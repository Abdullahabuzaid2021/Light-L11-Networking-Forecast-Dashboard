# L11 Networking Web App - Comprehensive Documentation

## Table of Contents
1. [README](#readme)
2. [Prompts Needed to Use](#prompts-needed-to-use)
3. [Sample Output](#sample-output)
4. [Demo Materials and Images](#demo-materials-and-images)
5. [Code Script](#code-script)
6. [Dashboard Usage Instructions](#dashboard-usage-instructions)
7. [Dell Team Access](#dell-team-access)
8. [Network Testing](#network-testing)

---

## README

### Overview
The L11 Networking Web App is a lightweight web application for L11 networking BOM (Bill of Materials) aggregation and analysis. It processes Excel files containing networking component data and provides an interactive dashboard for visualization and analysis.

### Features
- **Automated BOM Aggregation**: Processes multiple Excel files with PnL SN6600 tabs
- **Interactive Dashboard**: HTML/JavaScript dashboard with real-time data visualization
- **Project Breakdown Analysis**: Per-project quantity distribution across Horizon, CORE, and DH projects
- **Data Visualization**: Bar charts and pie charts with value labels
- **Search and Filtering**: Interactive tables with search functionality
- **Export Capabilities**: Export data in JSON format
- **Dell Integration**: SharePoint integration for team collaboration

### Technology Stack
- **Backend**: Python (pandas, openpyxl)
- **Frontend**: HTML, CSS, JavaScript
- **Visualization**: Chart.js with datalabels plugin
- **Server**: Python HTTP server
- **Data Processing**: Pandas for Excel file processing

### Repository Structure
```
L11_Networking_Web_App/
├── data/                          # Excel files directory
│   ├── Horizon PNL.xlsx
│   ├── P&L -IREN - 50MW 252 Racks - Sweetwater VR NVL72_SN6600-LD_CORE.xlsx
│   ├── P&L -IREN - 50MW 252 Racks - Sweetwater VR NVL72_SN6600-LD_DH.xlsx
│   └── total summary BOM per item.xlsx
├── simple_dashboard.html          # Simplified dashboard (recommended)
├── refresh_server.py              # Flask server with refresh API (recommended)
├── refresh_server_8080.py         # Alternative server on port 8080
├── refresh_server_80.py           # Alternative server on port 80
├── start_server.py                # Simple HTTP server (alternative)
├── process_data.py                # Python data processing script
├── network_test.py                # Network connectivity testing
├── requirements.txt               # Python dependencies
├── .nojekyll                     # Disables Jekyll for GitHub Pages
├── README.md                      # Project documentation
├── COMPREHENSIVE_DOCUMENTATION.md # Complete documentation
├── DELL_TEAM_ACCESS_GUIDE.md     # Dell team member guide
└── data.json                      # Generated data file
```

### Installation

#### Prerequisites
- Python 3.7 or higher
- pip package manager

#### Setup Instructions
1. Clone the repository:
```bash
git clone https://eos2git.cec.lab.emc.com/Abdullah-Abuzaid/Light-L11-Networking-Forecast-Dashboard.git
cd Light-L11-Networking-Forecast-Dashboard
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Place Excel files in the `data/` directory

### Quick Start

#### Data Processing
```bash
python process_data.py
```

#### Start Dashboard
```bash
python start_server.py
```

#### Access Dashboard
- **Local**: http://localhost:8000/simple_dashboard.html
- **Dell Network**: http://10.137.51.248:8000/simple_dashboard.html

### Dashboard Features

#### Summary Tab
- Overview of all networking components
- Total items, quantity, and files metrics
- Last updated timestamp

#### Files Tab
- Information about source Excel files
- File names, tabs, item counts, and modification dates

#### Project Breakdown Tab
- Per-project quantity distribution
- Columns for Horizon PNL.xlsx, CORE.xlsx, DH.xlsx
- Total column showing sum across all projects

#### Charts Tab
- Bar chart: Top 15 items by quantity with value labels
- Pie chart: Quantity distribution with percentages
- Interactive tooltips with detailed information

### Data Sources
- **SharePoint**: [Hackathon - L11 forecasting](https://dell.sharepoint.com/:f:/r/sites/NetworkingL11RackPlanning/Shared%20Documents/General/Hackathon%20-%20L11%20forecasting?d=wb9ae5c4571d84bec94d375ef7ea58856&csf=1&web=1&e=rBs2jB)
- **Repository Excel Files**: Located in `data/` directory

### Dell Internal Sharing
- **Network URL**: http://10.137.51.248:8000/simple_dashboard.html
- **External URL**: http://143.166.192.16:8000/simple_dashboard.html

### GitLab Repository
- **Repository**: https://eos2git.cec.lab.emc.com/Abdullah-Abuzaid/Light-L11-Networking-Forecast-Dashboard
- **GitHub Pages**: https://abdullahabuzaid2021.github.io/Light-L11-Networking-Forecast-Dashboard/

---

## Prompts Needed to Use

### Initial Setup Prompts

#### 1. Repository Setup
```
"Create a GitHub repository for L11 networking BOM aggregation web app with Python data processing and HTML dashboard"
```

#### 2. Data Processing Setup
```
"Create a Python script to process Excel files from the data/ directory and aggregate BOM data from PnL SN6600 tabs"
```

#### 3. Dashboard Development
```
"Create an HTML/JavaScript dashboard to visualize the processed networking BOM data with charts and tables"
```

### Data Processing Prompts

#### 4. Excel File Processing
```
"Process Excel files in the data/ directory and extract networking component data from PnL SN6600 tabs"
```

#### 5. Data Aggregation
```
"Aggregate the networking component data by Model/PN and calculate total quantities across all files"
```

#### 6. Project Breakdown
```
"Create a pivot table showing quantity distribution of networking components across different Excel files (Horizon, CORE, DH)"
```

### Dashboard Development Prompts

#### 7. Dashboard Layout
```
"Create a responsive HTML dashboard with tabs for Summary, Files, Project Breakdown, and Charts"
```

#### 8. Data Visualization
```
"Add bar chart showing top 15 networking items by quantity and pie chart showing quantity distribution"
```

#### 9. Value Labels
```
"Add value labels to charts so quantities are displayed directly on chart elements"
```

#### 10. Table Creation
```
"Create interactive tables for summary data, file information, and project breakdown with search functionality"
```

### Integration Prompts

#### 11. SharePoint Integration
```
"Add SharePoint link integration for Dell team collaboration and document the sharing process"
```

#### 12. Dell Network Sharing
```
"Configure the dashboard for Dell internal network sharing with appropriate URLs and access instructions"
```

### Troubleshooting Prompts

#### 13. Data Loading Issues
```
"Fix data loading issues in the dashboard by embedding data directly in HTML for immediate loading"
```

#### 14. Chart Enhancement
```
"Enhance charts to show values with proper formatting and add tooltips for detailed information"
```

### Documentation Prompts

#### 15. README Creation
```
"Create comprehensive README with installation instructions, usage guide, and feature documentation"
```

#### 16. User Guide
```
"Create detailed user guide with step-by-step instructions for dashboard usage and data processing"
```

---

## Sample Output

### Data Processing Output
```
============================================================
L11 Networking Data Processing
============================================================
Using Excel files from repository: C:\Users\Abdullah_Abuzaid\CascadeProjects\L11_Networking_Web_App\data

============================================================
Data processed successfully!
============================================================
Total items: 22
Total quantity: 449,774
Total files: 3
Data saved to: C:\Users\Abdullah_Abuzaid\CascadeProjects\L11_Networking_Web_App\data.json
Generated at: 2026-09-22 12:17:22
============================================================

Next steps:
1. Open index.html in your browser to view the dashboard
2. Or share the repository with your team
3. For updates: add new Excel files to data/ and re-run this script
```

### Dashboard Metrics Output
```
Total Items: 22
Total Quantity: 449,774
Total Files: 3
Last Updated: 2026-09-22 12:17:22
```

### Summary Table Sample
| Networking | Model/PN | Units |
|------------|----------|-------|
| MMS4B10-XM-RHS | MMS4B10-XM-RHS | 124,590 |
| MFP7E30-N050 | MFP7E30-N050 | 99,332 |
| MMS4B10-XM-RHS | 980-9IAJ0-00XM00 | 73,440 |
| MMS4X00-NM-T | MMS4X00-NM-T | 56,874 |
| MMS1X00-NS400 | MMS1X00-NS400 | 49,502 |

### Files Table Sample
| File | Tab | Items | Modified |
|------|-----|-------|----------|
| Horizon PNL.xlsx | PnL SN6600-_Horizon | 46 | 2026-09-22 09:46:46 |
| P&L -IREN - 50MW 252 Racks - Sweetwater VR NVL72_SN6600-LD_CORE.xlsx | PnL SN6600-LD | 14 | 2026-09-22 09:50:53 |
| P&L -IREN - 50MW 252 Racks - Sweetwater VR NVL72_SN6600-LD_DH.xlsx | PnL SN6600-LD-0831 | 20 | 2026-09-22 09:44:19 |

### Project Breakdown Table Sample
| Networking | Horizon PNL.xlsx | CORE.xlsx | DH.xlsx | Total |
|------------|-----------------|-----------|---------|-------|
| MMS4B10-XM-RHS | 124,590 | 0 | 0 | 124,590 |
| MFP7E30-N050 | 0 | 2,232 | 97,100 | 99,332 |
| MMS4X00-NM-T | 36,326 | 2,616 | 17,932 | 56,874 |
| MMS1X00-NS400 | 30,662 | 1,056 | 17,784 | 49,502 |

### Chart Data Sample
```json
{
  "summary": [
    {
      "Networking": "MMS4B10-XM-RHS",
      "Model/PN": "MMS4B10-XM-RHS",
      "Units": 124590.0
    },
    {
      "Networking": "MFP7E30-N050",
      "Model/PN": "MFP7E30-N050",
      "Units": 99332.0
    }
  ],
  "total_items": 22,
  "total_quantity": 449774,
  "total_files": 3
}
```

---

## Demo Materials and Images

### Dashboard Screenshots

#### 1. Dashboard Overview
```
[Dashboard Header]
🌐 L11 Networking Forecast Dashboard
Interactive BOM aggregation and analysis for L11 networking components

[Data Status]
📊 Data Status: ✅ Loaded from repository Excel files
📁 Data Source: Excel files in repository data/ directory
🔗 SharePoint: Hackathon - L11 forecasting

[Metrics Cards]
Total Items: 22
Total Quantity: 449,774
Total Files: 3
Last Updated: 2026-09-22 12:17:22
```

#### 2. Summary Tab
```
[Summary Table]
Networking           | Model/PN            | Units
---------------------|---------------------|--------
MMS4B10-XM-RHS       | MMS4B10-XM-RHS      | 124,590
MFP7E30-N050         | MFP7E30-N050        | 99,332
MMS4B10-XM-RHS       | 980-9IAJ0-00XM00    | 73,440
MMS4X00-NM-T         | MMS4X00-NM-T        | 56,874
MMS1X00-NS400        | MMS1X00-NS400       | 49,502
```

#### 3. Project Breakdown Tab
```
[Project Breakdown Table]
Networking           | Horizon PNL.xlsx | CORE.xlsx | DH.xlsx | Total
---------------------|------------------|-----------|---------|--------
MMS4B10-XM-RHS       | 124,590          | 0         | 0       | 124,590
MFP7E30-N050         | 0                | 2,232     | 97,100  | 99,332
MMS4X00-NM-T         | 36,326           | 2,616     | 17,932  | 56,874
```

#### 4. Charts Tab
```
[Bar Chart]
Top 15 Items by Quantity
[Bars with value labels showing: 124,590, 99,332, 73,440, etc.]

[Pie Chart]
Quantity Distribution (Top 10 Items)
[Slices with labels showing: "124,590 (27.7%)", "99,332 (22.1%)", etc.]
```

### Data Flow Diagram
```
Excel Files (data/)
    ↓
process_data.py
    ↓
data.json
    ↓
simple_dashboard.html
    ↓
Browser Visualization
```

### Architecture Diagram
```
┌─────────────────────────────────────────┐
│         Repository Structure             │
├─────────────────────────────────────────┤
│  data/                                  │
│  ├── Horizon PNL.xlsx                   │
│  ├── CORE.xlsx                          │
│  └── DH.xlsx                            │
│                                         │
│  process_data.py (Python)               │
│  start_server.py (Python)               │
│  simple_dashboard.html (HTML/JS)       │
│  data.json (Generated)                  │
└─────────────────────────────────────────┘
```

### User Workflow
```
1. User adds Excel files to data/ directory
2. User runs: python process_data.py
3. User runs: python start_server.py
4. User opens: http://localhost:8000/simple_dashboard.html
5. User views interactive dashboard
6. User shares Dell network URL with team
```

---

## Code Script

### Data Processing Script (process_data.py)

This is the main Python script that processes Excel files before dashboard visualization:

```python
#!/usr/bin/env python3
"""
L11 Networking Data Processing Script
Processes Excel files from data/ directory and aggregates BOM data
"""

import pandas as pd
import json
from pathlib import Path
from datetime import datetime

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
                            summary_keywords = ['Total Data Hall', 'Total Core', 'Total Horizon', 
                                             'Data Hall E-W', 'Data Hall N-S', 'Data Hall OOB', 
                                             'Core E-W', 'Core N-S', 'Core OOB', 'Rack Integration']
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
    script_dir = Path(__file__).parent.resolve()
    local_data_dir = script_dir / "data"
    
    print("=" * 60)
    print("L11 Networking Data Processing")
    print("=" * 60)
    print(f"Using Excel files from repository: {local_data_dir}")
    
    # Process the data directly from repository
    summary_df, files_df, pivot_df, combined_df, error = process_bom_data(str(local_data_dir))
    
    if error:
        print(f"❌ Error: {error}")
    else:
        # Generate JSON data
        json_data = generate_json_data(summary_df, files_df, pivot_df, combined_df)
        
        # Save JSON data
        json_file = script_dir / 'data.json'
        with open(json_file, 'w') as f:
            json.dump(json_data, f, indent=2)
        
        print("\n" + "=" * 60)
        print("Data processed successfully!")
        print("=" * 60)
        print(f"Total items: {json_data['total_items']}")
        print(f"Total quantity: {json_data['total_quantity']:,}")
        print(f"Total files: {json_data['total_files']}")
        print(f"Data saved to: {json_file}")
        print(f"Generated at: {json_data['generated_at']}")
        print("=" * 60)
```

### Flask Server Script (refresh_server.py)

```python
#!/usr/bin/env python3
"""
Flask server for L11 Networking Dashboard with refresh functionality
Provides API endpoint for data refresh and serves dashboard files
"""

from flask import Flask, jsonify, send_from_directory
from pathlib import Path
import subprocess
import json
from datetime import datetime

app = Flask(__name__)
BASE_DIR = Path(__file__).parent.resolve()

def process_data():
    """Run the data processing script"""
    try:
        result = subprocess.run(
            ['python', 'process_data.py'],
            cwd=BASE_DIR,
            capture_output=True,
            text=True,
            timeout=60
        )
        
        data_file = BASE_DIR / 'data.json'
        if data_file.exists():
            with open(data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            return {
                'success': True,
                'message': 'Data processed successfully',
                'total_items': data.get('total_items', 0),
                'total_quantity': data.get('total_quantity', 0),
                'total_files': data.get('total_files', 0),
                'generated_at': data.get('generated_at', datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
                'output': result.stdout
            }
        else:
            return {
                'success': False,
                'message': 'Data processing completed but data.json not found',
                'output': result.stdout,
                'error': result.stderr
            }
    except subprocess.TimeoutExpired:
        return {
            'success': False,
            'message': 'Data processing timed out',
            'error': 'Processing took longer than 60 seconds'
        }
    except Exception as e:
        return {
            'success': False,
            'message': f'Error processing data: {str(e)}',
            'error': str(e)
        }

@app.route('/')
def serve_index():
    """Serve the main dashboard"""
    return send_from_directory(BASE_DIR, 'simple_dashboard.html')

@app.route('/simple_dashboard.html')
def serve_dashboard():
    """Serve the dashboard"""
    return send_from_directory(BASE_DIR, 'simple_dashboard.html')

@app.route('/data.json')
def serve_data():
    """Serve the data file"""
    return send_from_directory(BASE_DIR, 'data.json')

@app.route('/api/refresh', methods=['POST'])
def refresh_data():
    """API endpoint to refresh data"""
    result = process_data()
    return jsonify(result)

@app.route('/api/status')
def get_status():
    """Get current data status"""
    data_file = BASE_DIR / 'data.json'
    
    if data_file.exists():
        with open(data_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        return jsonify({
            'success': True,
            'total_items': data.get('total_items', 0),
            'total_quantity': data.get('total_quantity', 0),
            'total_files': data.get('total_files', 0),
            'generated_at': data.get('generated_at', 'Unknown')
        })
    else:
        return jsonify({
            'success': False,
            'message': 'Data file not found. Run process_data.py first.'
        })

if __name__ == '__main__':
    print("=" * 60)
    print("L11 Networking Dashboard Server with Refresh API")
    print("=" * 60)
    print(f"Server directory: {BASE_DIR}")
    print(f"Dashboard URL: http://localhost:8000/simple_dashboard.html")
    print(f"Network URL: http://10.137.51.248:8000/simple_dashboard.html")
    print(f"Refresh API: http://localhost:8000/api/refresh")
    print("=" * 60)
    print("Press Ctrl+C to stop the server")
    print("=" * 60)
    
    app.run(host='0.0.0.0', port=8000, debug=False)
```

### Network Testing Script (network_test.py)

```python
#!/usr/bin/env python3
"""
Network Connectivity Test Script for L11 Networking Dashboard
Tests network connectivity and server accessibility
"""

import socket
import subprocess
import sys
from pathlib import Path
import requests
import json

def test_local_server():
    """Test if local server is running"""
    print("=" * 60)
    print("Testing Local Server")
    print("=" * 60)
    
    try:
        response = requests.get('http://localhost:8000/simple_dashboard.html', timeout=10)
        if response.status_code == 200:
            print("[PASS] Local server is running and accessible")
            print(f"   Status: {response.status_code}")
            print(f"   URL: http://localhost:8000/simple_dashboard.html")
            return True
        else:
            print(f"[FAIL] Local server returned status: {response.status_code}")
            return False
    except requests.exceptions.Timeout:
        print("[WARN] Local server timeout - server may be slow but running")
        print("   Server is likely running but responding slowly")
        return True
    except requests.exceptions.ConnectionError:
        print("[FAIL] Local server is not running")
        print("   Start the server with: python refresh_server.py")
        return False
    except Exception as e:
        print(f"[FAIL] Error testing local server: {e}")
        return False

def test_network_ip():
    """Test network IP accessibility"""
    print("\n" + "=" * 60)
    print("Testing Network IP (10.137.51.248)")
    print("=" * 60)
    
    ip = "10.137.51.248"
    port = 8000
    
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((ip, port))
        
        if result == 0:
            print("[PASS] Network IP is accessible")
            print(f"   IP: {ip}")
            print(f"   Port: {port}")
            print(f"   URL: http://{ip}:{port}/simple_dashboard.html")
            sock.close()
            return True
        else:
            print(f"[FAIL] Cannot connect to {ip}:{port}")
            print("   Possible causes:")
            print("   - Server not running")
            print("   - Network firewall blocking connection")
            print("   - Incorrect IP address")
            sock.close()
            return False
    except socket.gaierror:
        print(f"[FAIL] Cannot resolve hostname: {ip}")
        return False
    except Exception as e:
        print(f"[FAIL] Error testing network IP: {e}")
        return False

if __name__ == "__main__":
    print("L11 Networking Dashboard - Network Connectivity Test")
    print("=" * 60)
    
    results = {
        'local_server': test_local_server(),
        'network_ip': test_network_ip()
    }
    
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    
    for test_name, result in results.items():
        status = "[PASS]" if result else "[FAIL]"
        print(f"{status}: {test_name.replace('_', ' ').title()}")
    
    print("=" * 60)
```

### Key Scripts in Repository

| Script | Purpose | Usage |
|--------|---------|-------|
| **process_data.py** | Main data processing script | `python process_data.py` |
| **refresh_server.py** | Flask server with refresh API (port 8000) | `python refresh_server.py` |
| **refresh_server_8080.py** | Alternative server on port 8080 | `python refresh_server_8080.py` |
| **refresh_server_80.py** | Alternative server on port 80 | `python refresh_server_80.py` |
| **start_server.py** | Simple HTTP server (no refresh) | `python start_server.py` |
| **network_test.py** | Network connectivity testing | `python network_test.py` |
        print("2. Or share the repository with your team")
        print("3. For updates: add new Excel files to data/ and re-run this script")
    else:
        print("No data processed. Please check Excel files in data/ directory.")
```

### start_server.py
```python
#!/usr/bin/env python3
"""
Simple HTTP Server for L11 Networking Dashboard
Starts a local HTTP server to serve the dashboard files
"""

import http.server
import socketserver
import webbrowser
from pathlib import Path

def start_server(port=8000):
    """Start HTTP server and open dashboard"""
    script_dir = Path(__file__).parent
    
    class Handler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=str(script_dir), **kwargs)
    
    try:
        with socketserver.TCPServer(("", port), Handler) as httpd:
            print(f"Server started at http://localhost:{port}")
            print(f"Dashboard available at http://localhost:{port}/simple_dashboard.html")
            print(f"Press Ctrl+C to stop the server")
            
            # Open dashboard in browser
            webbrowser.open(f'http://localhost:{port}/simple_dashboard.html')
            
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped")
    except OSError as e:
        print(f"Error starting server: {e}")
        print(f"Port {port} may be in use. Try a different port.")

if __name__ == "__main__":
    start_server()
```

### requirements.txt
```
pandas>=1.3.0
openpyxl>=3.0.0
```

### simple_dashboard.html (Key Sections)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>L11 Networking Forecast Dashboard</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-datalabels@2.0.0"></script>
    <style>
        /* CSS styles for responsive dashboard */
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🌐 L11 Networking Forecast Dashboard</h1>
        </div>
        
        <div class="metrics">
            <!-- Metric cards -->
        </div>
        
        <div class="tabs">
            <button class="tab active" onclick="showTab('summary')">📋 Summary</button>
            <button class="tab" onclick="showTab('files')">📁 Files</button>
            <button class="tab" onclick="showTab('breakdown')">📊 Project Breakdown</button>
            <button class="tab" onclick="showTab('charts')">📈 Charts</button>
        </div>
        
        <div id="summary" class="tab-content active">
            <!-- Summary table -->
        </div>
        
        <div id="files" class="tab-content">
            <!-- Files table -->
        </div>
        
        <div id="breakdown" class="tab-content">
            <!-- Project breakdown table -->
        </div>
        
        <div id="charts" class="tab-content">
            <!-- Charts -->
        </div>
    </div>
    
    <script>
        // Embedded data from repository Excel files
        const dashboardData = {...};
        
        // Dashboard initialization and chart creation
    </script>
</body>
</html>
```

---

## Dashboard Usage Instructions

### Getting Started

#### Step 1: Prepare Excel Files
1. Place your Excel files in the `data/` directory
2. Ensure files contain PnL SN6600 tabs with networking component data
3. Verify files have columns: Networking, Model/PN, Units

#### Step 2: Process Data
```bash
cd L11_Networking_Web_App
python process_data.py
```

**Expected Output:**
```
============================================================
L11 Networking Data Processing
============================================================
Using Excel files from repository: /path/to/data

============================================================
Data processed successfully!
============================================================
Total items: 22
Total quantity: 449,774
Total files: 3
Data saved to: /path/to/data.json
Generated at: 2026-09-22 12:17:22
============================================================
```

#### Step 3: Start Dashboard
```bash
python start_server.py
```

**Expected Output:**
```
Server started at http://localhost:8000
Dashboard available at http://localhost:8000/simple_dashboard.html
Press Ctrl+C to stop the server
```

#### Step 4: Access Dashboard
- **Local**: http://localhost:8000/simple_dashboard.html
- **Dell Network**: http://10.137.51.248:8000/simple_dashboard.html

### Dashboard Navigation

#### Summary Tab
- **Purpose**: View aggregated networking component data
- **Features**:
  - Total items, quantity, and files metrics
  - Complete list of networking components
  - Model/PN and unit quantities
  - Last updated timestamp

#### Files Tab
- **Purpose**: View source Excel file information
- **Features**:
  - File names and tabs processed
  - Item counts per file
  - Modification dates
  - Data source tracking

#### Project Breakdown Tab
- **Purpose**: Analyze quantity distribution across projects
- **Features**:
  - Per-project quantities (Horizon, CORE, DH)
  - Total column showing sum across projects
  - Color-coded totals for emphasis
  - Easy comparison of project distribution

#### Charts Tab
- **Purpose**: Visualize data with interactive charts
- **Features**:
  - **Bar Chart**: Top 15 items by quantity
    - Value labels on bars
    - Hover tooltips with details
    - Y-axis with formatted numbers
  - **Pie Chart**: Quantity distribution (Top 10)
    - Value and percentage labels
    - Color-coded segments
    - Interactive hover effects

### Data Updates

#### Adding New Excel Files
1. Place new Excel files in `data/` directory
2. Run `python process_data.py`
3. Refresh the dashboard in browser

#### Updating Existing Data
1. Modify Excel files in `data/` directory
2. Run `python process_data.py`
3. Refresh the dashboard in browser

#### Refreshing Dashboard
- **Method 1**: Click browser refresh button
- **Method 2**: Press F5
- **Method 3**: Ctrl+R (Windows) or Cmd+R (Mac)

### Dell Team Sharing

#### Internal Network Sharing
1. Start the dashboard server
2. Share the network URL: http://10.137.51.248:8000/simple_dashboard.html
3. Team members can access within Dell network

#### External Access
1. Share external URL: http://143.166.192.16:8000/simple_dashboard.html
2. Ensure firewall rules allow external access
3. Team members can access from outside Dell network

#### GitHub Pages Sharing
1. Push code to GitHub repository
2. Enable GitHub Pages in repository settings
3. Share GitHub Pages URL with team
4. Automatic deployment on code updates

### Troubleshooting

#### Dashboard Not Loading
**Problem**: Dashboard shows "Error loading data"
**Solution**:
1. Run `python process_data.py` to generate data.json
2. Check that data.json exists in repository root
3. Verify server is running with `python start_server.py`

#### Charts Not Displaying
**Problem**: Charts show blank or error
**Solution**:
1. Check browser console for JavaScript errors (F12)
2. Verify Chart.js CDN is accessible
3. Ensure data.json contains valid JSON structure

#### Data Not Updating
**Problem**: Dashboard shows old data after processing
**Solution**:
1. Clear browser cache (Ctrl+Shift+Delete)
2. Hard refresh (Ctrl+Shift+R)
3. Verify data.json was regenerated

#### Server Won't Start
**Problem**: "Port 8000 is already in use"
**Solution**:
1. Stop existing server process
2. Use different port: modify start_server.py
3. Check for other applications using port 8000

### Advanced Usage

#### Custom Data Processing
Modify `process_data.py` to:
- Add custom aggregation logic
- Include additional data fields
- Implement filtering rules
- Add data validation

#### Dashboard Customization
Modify `simple_dashboard.html` to:
- Change color schemes
- Add custom metrics
- Implement additional charts
- Add export functionality

#### Integration with Other Systems
- **SharePoint**: Sync Excel files via SharePoint client
- **API Integration**: Add REST API endpoints for data access
- **Database**: Store processed data in database for persistence
- **Automation**: Schedule automated data processing

### Performance Optimization

#### Large Datasets
- Process Excel files in batches
- Implement pagination for tables
- Use data sampling for charts
- Enable lazy loading

#### Server Performance
- Use production web server (nginx, Apache)
- Implement caching strategies
- Optimize data processing algorithms
- Use CDN for static assets

### Security Considerations

#### Data Security
- Don't commit sensitive data to repository
- Use environment variables for configuration
- Implement access controls for shared dashboards
- Regular security updates for dependencies

#### Network Security
- Use HTTPS for production deployments
- Implement authentication for dashboard access
- Configure firewall rules appropriately
- Monitor access logs

### Best Practices

#### Data Management
- Keep Excel files in version control
- Document data sources and transformations
- Implement data validation rules
- Regular data quality checks

#### Dashboard Maintenance
- Regular updates to dependencies
- Monitor dashboard performance
- Gather user feedback for improvements
- Document customizations and changes

#### Team Collaboration
- Share clear usage instructions
- Provide training for team members
- Establish data update schedules
- Create troubleshooting guides

---

## Additional Resources

### Documentation
- [Project README](README.md)
- [GitHub Repository](https://eos2git.cec.lab.emc.com/Abdullah-Abuzaid/Light-L11-Networking-Forecast-Dashboard)
- [SharePoint Documentation](https://dell.sharepoint.com/:f:/r/sites/NetworkingL11RackPlanning/Shared%20Documents/General/Hackathon%20-%20L11%20forecasting)

### Support
- **Dell Internal**: Contact Networking L11 Rack Planning team
- **GitHub Issues**: Report bugs and feature requests
- **Documentation**: Check this document for common issues

### Version History
- **v1.0** - Initial release with basic dashboard
- **v1.1** - Added project breakdown table
- **v1.2** - Enhanced charts with value labels
- **v1.3** - Improved data embedding and loading

---

## Dell Team Access

### Primary Access Method: GitHub Pages (RECOMMENDED)

**Dashboard URL**: https://abdullahabuzaid2021.github.io/Light-L11-Networking-Forecast-Dashboard/simple_dashboard.html

#### Advantages
- ✅ **No admin rights required**
- ✅ **No network restrictions** - works globally
- ✅ **No software installation needed**
- ✅ **Automatic deployment** on git push
- ✅ **Permanent URL** - always available
- ✅ **No firewall configuration** needed

#### System Requirements
- **Web browser**: Chrome, Firefox, Edge, or Safari (latest version)
- **Internet connection**: Any internet connection
- **JavaScript enabled**: Required for dashboard functionality
- **No special software**: No installation needed

#### How to Access
1. **Open web browser**
2. **Navigate to**: GitHub Pages URL above
3. **Dashboard loads** automatically
4. **Use all features** immediately

### Alternative: Dell Internal Network Access

**Network URL**: http://10.137.51.248:8000/simple_dashboard.html
**Alternative Port**: http://10.137.51.248:8080/simple_dashboard.html

#### Prerequisites
- **Must be connected to Dell internal network** (amer.dell.com domain)
- **VPN access** if working remotely
- **Dell corporate credentials** for network authentication
- **Firewall permissions** to access port 8000 or 8080
- **Admin rights** may be required to configure Windows Firewall

#### Important Note
Dell network access requires **firewall configuration** on the server machine. If you cannot access the network URL, use GitHub Pages as the primary method to avoid firewall issues.

### Troubleshooting GitHub Pages Access

#### Common Issues
1. **"404 Not Found"**: Wait 2-3 minutes for deployment, verify URL
2. **"Loading Data..."**: Hard refresh (Ctrl+Shift+R), clear browser cache
3. **Charts Not Displaying**: Enable JavaScript, try different browser
4. **Deployment Errors**: Check Actions tab in GitHub repository

#### Solutions
1. **Hard refresh**: Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac)
2. **Clear browser cache**: Clear cache and cookies
3. **Check browser console**: Press F12 to check for JavaScript errors
4. **Contact dashboard owner**: Verify data was processed and committed

### Dell Team Access Guide

For detailed instructions, see [DELL_TEAM_ACCESS_GUIDE.md](DELL_TEAM_ACCESS_GUIDE.md) which includes:
- Complete setup instructions for Dell team members
- Network troubleshooting procedures
- VPN setup for remote users
- Mobile access guidelines
- Security considerations
- Support and contact information

## Network Testing

### Network Test Script

The repository includes `network_test.py` for automated network connectivity testing:

```bash
python network_test.py
```

### Test Coverage

The script tests:
- **Local Server Status**: Verifies dashboard server is running
- **Network IP Accessibility**: Tests 10.137.51.248:8000 connectivity
- **Data File Validation**: Checks data.json exists and is valid
- **Excel Files Presence**: Verifies Excel files in data/ directory
- **Firewall Rules**: Tests port 8000 accessibility

### Test Results Interpretation

#### PASS Results
- **[PASS] Local Server**: Dashboard server is running and accessible
- **[PASS] Network IP**: Network IP is accessible for team sharing
- **[PASS] Data File**: Data file exists and contains valid data
- **[PASS] Excel Files**: Excel files found in data/ directory
- **[PASS] Firewall**: Port 8000 is accessible, no firewall blocking

#### FAIL Results
- **[FAIL] Local Server**: Start server with `python start_server.py`
- **[FAIL] Network IP**: Check network connectivity and firewall settings
- **[FAIL] Data File**: Run `python process_data.py` to generate data
- **[FAIL] Excel Files**: Add Excel files to data/ directory
- **[FAIL] Firewall**: Check firewall rules and port availability

### Network Diagnostics

#### Manual Testing Commands
```bash
# Test network connectivity
ping 10.137.51.248

# Test port accessibility
telnet 10.137.51.248 8000

# Test HTTP access
curl http://10.137.51.248:8000/

# Check network configuration
ipconfig /all
```

#### Browser Testing
1. Open browser
2. Navigate to: http://10.137.51.248:8000/simple_dashboard.html
3. Check if dashboard loads correctly
4. Open browser console (F12) to check for errors

### Access Report

The network test script generates a comprehensive access report including:
- **Local IP**: Your machine's IP address
- **Network IP**: 10.137.51.248 for Dell team sharing
- **Port**: 8000 for dashboard access
- **Access URLs**: All available URLs for dashboard access
- **Dell Team Requirements**: Prerequisites for team members

## Conclusion

This comprehensive documentation provides all necessary information for setting up, using, and maintaining the L11 Networking Web App. The application successfully processes Excel files from the repository, aggregates networking BOM data, and provides an interactive dashboard for analysis and team collaboration within Dell's environment.

### Key Features
- **Automated Data Processing**: Processes Excel files from repository
- **Interactive Dashboard**: HTML/JavaScript with embedded data
- **Dell Network Sharing**: Configured for internal team access
- **Network Testing**: Automated connectivity verification
- **Comprehensive Documentation**: Complete guides for all users

### Team Sharing
- **Dell Internal Network**: http://10.137.51.248:8000/simple_dashboard.html
- **GitHub Pages**: Available for external access
- **Complete Documentation**: Guides for team members and administrators

For questions or issues, please refer to the troubleshooting section, Dell Team Access Guide, or contact the development team.