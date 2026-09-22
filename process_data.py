import pandas as pd
import json
from pathlib import Path
from datetime import datetime
import os

def process_bom_data(directory):
    """Process all Excel files and aggregate BOM data from PnL SN6600 tabs"""
    all_data = []
    file_info = []
    
    try:
        dir_path = Path(directory)
        if not dir_path.exists():
            return None, None, "Directory not found"
        
        # Iterate through all Excel files in the directory
        for file_path in dir_path.glob('*.xlsx'):
            file_name = file_path.name
            file_modified = datetime.fromtimestamp(file_path.stat().st_mtime)
            
            # Load the Excel file
            try:
                xl = pd.ExcelFile(file_path)
                
                # Find tabs that include "PnL SN6600" in their name
                pnl_tabs = [sheet for sheet in xl.sheet_names if 'PnL SN6600' in sheet]
                
                for tab_name in pnl_tabs:
                    # Read the tab with no header to find the header row
                    df = pd.read_excel(file_path, sheet_name=tab_name, header=None)
                    
                    # Find the header row (row containing 'Model/PN')
                    header_row = None
                    for idx, row in df.iterrows():
                        if 'Model/PN' in row.values:
                            header_row = idx
                            break
                    
                    if header_row is not None:
                        # Read the data with the correct header
                        df = pd.read_excel(file_path, sheet_name=tab_name, header=header_row)
                        
                        # Extract relevant columns
                        if 'Model/PN' in df.columns and 'Units' in df.columns:
                            # Add source file and tab information
                            df['Source File'] = file_name
                            df['Source Tab'] = tab_name
                            df['File Modified'] = file_modified
                            
                            # Add Networking column if it doesn't exist
                            if 'Networking' not in df.columns:
                                df['Networking'] = 'N/A'
                            
                            # Select only the columns we need
                            relevant_data = df[['Networking', 'Model/PN', 'Units', 'Source File', 'Source Tab', 'File Modified']].copy()
                            
                            # Remove rows where Model/PN is NaN
                            relevant_data = relevant_data[relevant_data['Model/PN'].notna()]
                            
                            # Convert Units to numeric, coerce errors to NaN
                            relevant_data['Units'] = pd.to_numeric(relevant_data['Units'], errors='coerce')
                            
                            # Remove rows where Units is NaN or 0
                            relevant_data = relevant_data[relevant_data['Units'].notna()]
                            relevant_data = relevant_data[relevant_data['Units'] != 0]
                            
                            # Filter out summary sections
                            summary_keywords = ['Total Data Hall', 'Total Core', 'Total Horizon', 'Data Hall E-W', 'Data Hall N-S', 'Data Hall OOB', 'Core E-W', 'Core N-S', 'Core OOB', 'Rack Integration']
                            relevant_data = relevant_data[~relevant_data['Model/PN'].isin(summary_keywords)]
                            relevant_data = relevant_data[~relevant_data['Model/PN'].str.startswith('Total ', na=False)]
                            
                            all_data.append(relevant_data)
                            file_info.append({
                                'File': file_name,
                                'Tab': tab_name,
                                'Items': len(relevant_data),
                                'Modified': file_modified.strftime('%Y-%m-%d %H:%M:%S')
                            })
            
            except Exception as e:
                print(f"Error processing {file_name}: {e}")
                continue
        
        if all_data:
            # Combine all data
            combined_df = pd.concat(all_data, ignore_index=True)
            
            # Ensure proper data types
            combined_df['Model/PN'] = combined_df['Model/PN'].astype(str)
            combined_df['Networking'] = combined_df['Networking'].astype(str)
            combined_df['Source File'] = combined_df['Source File'].astype(str)
            
            # Aggregate by Model/PN - sum the Units and get the Networking value
            summary_df = combined_df.groupby('Model/PN').agg({
                'Networking': 'first',
                'Units': 'sum'
            }).reset_index()
            
            # Filter out items with total Units = 0
            summary_df = summary_df[summary_df['Units'] != 0]
            
            # Sort by Units descending
            summary_df = summary_df.sort_values('Units', ascending=False)
            
            # Reorder columns: Networking, Model/PN, Units
            summary_df = summary_df[['Networking', 'Model/PN', 'Units']]
            
            # Create file info dataframe
            files_df = pd.DataFrame(file_info)
            
            # Create pivot table for project breakdown
            pivot_df = combined_df.pivot_table(
                index='Model/PN',
                columns='Source File',
                values='Units',
                aggfunc='sum',
                fill_value=0
            )
            
            # Add total column
            pivot_df['Total'] = pivot_df.sum(axis=1)
            
            # Sort by total descending
            pivot_df = pivot_df.sort_values('Total', ascending=False)
            
            # Add Networking description back to the pivot table
            networking_map = combined_df.drop_duplicates('Model/PN').set_index('Model/PN')['Networking'].to_dict()
            pivot_df.insert(0, 'Networking', pivot_df.index.map(networking_map))
            
            return summary_df, files_df, pivot_df, combined_df, None
        else:
            return None, None, None, None, "No PnL SN6600 tabs found in any files"
            
    except Exception as e:
        return None, None, None, None, f"Error processing data: {str(e)}"

def generate_json_data(summary_df, files_df, pivot_df, combined_df):
    """Convert dataframes to JSON format for web display"""
    # Convert dataframes to records and handle datetime serialization
    summary_records = summary_df.to_dict('records')
    files_records = files_df.to_dict('records') if files_df is not None else []
    pivot_records = pivot_df.to_dict('records') if pivot_df is not None else []
    
    # Convert any datetime objects to strings in combined data
    combined_records = []
    for record in combined_df.to_dict('records'):
        record_copy = record.copy()
        for key, value in record_copy.items():
            if hasattr(value, 'strftime'):  # Check if it's a datetime object
                record_copy[key] = value.strftime('%Y-%m-%d %H:%M:%S')
        combined_records.append(record_copy)
    
    data = {
        'summary': summary_records,
        'files': files_records,
        'pivot': pivot_records,
        'combined': combined_records,
        'generated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'total_items': len(summary_df),
        'total_quantity': int(summary_df['Units'].sum()),
        'total_files': len(files_df['File'].unique()) if files_df is not None else 0
    }
    return data

if __name__ == "__main__":
    # Default directory - use data directory in the project
    script_dir = Path(__file__).parent.resolve()
    default_dir = str(script_dir / "data")
    
    # Process data
    summary_df, files_df, pivot_df, combined_df, error = process_bom_data(default_dir)
    
    if error:
        print(f"Error: {error}")
    else:
        # Generate JSON data
        json_data = generate_json_data(summary_df, files_df, pivot_df, combined_df)
        
        # Save JSON data
        with open('data.json', 'w') as f:
            json.dump(json_data, f, indent=2)
        
        print("Data processed successfully!")
        print(f"Total items: {json_data['total_items']}")
        print(f"Total quantity: {json_data['total_quantity']:,}")
        print(f"Total files: {json_data['total_files']}")
        print("Data saved to data.json")
