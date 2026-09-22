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
│   └── P&L -IREN - 50MW 252 Racks - Sweetwater VR NVL72_SN6600-LD_DH.xlsx
├── index.html                     # Original dashboard (complex)
├── simple_dashboard.html          # Simplified dashboard (recommended)
├── process_data.py                # Python data processing script
├── start_server.py                # HTTP server starter
├── requirements.txt               # Python dependencies
├── README.md                      # Project documentation
└── data.json                      # Generated data file
```

### Installation

#### Prerequisites
- Python 3.7 or higher
- pip package manager

#### Setup Instructions
1. Clone the repository:
```bash
git clone https://github.com/Abdullahabuzaid2021/Lightweight-web-app-for-L11-networking-BOM-aggregation---uses-repository-Excel-files.git
cd Lightweight-web-app-for-L11-networking-BOM-aggregation---uses-repository-Excel-files
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

### GitHub Repository
- **Repository**: https://github.com/Abdullahabuzaid2021/Lightweight-web-app-for-L11-networking-BOM-aggregation---uses-repository-Excel-files
- **GitHub Pages**: https://abdullahabuzaid2021.github.io/Lightweight-web-app-for-L11-networking-BOM-aggregation---uses-repository-Excel-files/

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

### process_data.py
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

def process_excel_files(data_dir):
    """Process all Excel files in the data directory"""
    all_data = []
    file_info = []
    
    excel_files = list(data_dir.glob("*.xlsx"))
    print(f"Found {len(excel_files)} Excel files")
    
    for file in excel_files:
        try:
            print(f"Processing: {file.name}")
            df = pd.read_excel(file)
            
            # Look for PnL SN6600 tabs
            pnl_tabs = [col for col in df.columns if 'PnL' in str(col) or 'SN6600' in str(col)]
            
            if pnl_tabs:
                # Extract relevant columns
                relevant_cols = ['Networking', 'Model/PN', 'Units']
                available_cols = [col for col in relevant_cols if col in df.columns]
                
                if available_cols:
                    df_filtered = df[available_cols].copy()
                    df_filtered['Source File'] = file.name
                    df_filtered['File Modified'] = datetime.fromtimestamp(file.stat().st_mtime).strftime('%Y-%m-%d %H:%M:%S')
                    
                    all_data.append(df_filtered)
                    
                    file_info.append({
                        'File': file.name,
                        'Tab': pnl_tabs[0] if pnl_tabs else 'Unknown',
                        'Items': len(df_filtered),
                        'Modified': datetime.fromtimestamp(file.stat().st_mtime).strftime('%Y-%m-%d %H:%M:%S')
                    })
                    
                    print(f"  - Extracted {len(df_filtered)} items")
        except Exception as e:
            print(f"Error processing {file.name}: {e}")
    
    if all_data:
        combined_df = pd.concat(all_data, ignore_index=True)
        return combined_df, file_info
    return None, []

def aggregate_data(df):
    """Aggregate data by Model/PN"""
    if df is None:
        return None
    
    # Aggregate by Model/PN
    summary = df.groupby(['Networking', 'Model/PN'])['Units'].sum().reset_index()
    summary = summary.sort_values('Units', ascending=False)
    
    return summary

def create_pivot_table(df):
    """Create pivot table for project breakdown"""
    if df is None:
        return None
    
    # Create pivot table
    pivot = df.pivot_table(
        index='Networking',
        columns='Source File',
        values='Units',
        aggfunc='sum',
        fill_value=0
    ).reset_index()
    
    # Add total column
    pivot['Total'] = pivot.sum(axis=1, numeric_only=True)
    
    return pivot

def save_data(data, output_file):
    """Save processed data to JSON file"""
    output_data = {
        'summary': data['summary'].to_dict('records'),
        'files': data['files'],
        'pivot': data['pivot'].to_dict('records'),
        'combined': data['combined'].to_dict('records'),
        'total_items': len(data['summary']),
        'total_quantity': data['summary']['Units'].sum(),
        'total_files': len(data['files']),
        'generated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)
    
    print(f"Data saved to: {output_file}")

if __name__ == "__main__":
    script_dir = Path(__file__).parent.resolve()
    local_data_dir = script_dir / "data"
    
    print("=" * 60)
    print("L11 Networking Data Processing")
    print("=" * 60)
    print(f"Using Excel files from repository: {local_data_dir}")
    
    # Process the data directly from repository
    combined_df, file_info = process_excel_files(local_data_dir)
    
    if combined_df is not None:
        # Aggregate data
        summary = aggregate_data(combined_df)
        pivot = create_pivot_table(combined_df)
        
        # Prepare data for JSON export
        data = {
            'summary': summary,
            'files': file_info,
            'pivot': pivot,
            'combined': combined_df
        }
        
        # Save to JSON
        output_file = script_dir / "data.json"
        save_data(data, output_file)
        
        print("=" * 60)
        print("Data processed successfully!")
        print("=" * 60)
        print(f"Total items: {len(summary)}")
        print(f"Total quantity: {summary['Units'].sum():,.0f}")
        print(f"Total files: {len(file_info)}")
        print(f"Data saved to: {output_file}")
        print(f"Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 60)
        print("\nNext steps:")
        print("1. Open simple_dashboard.html in your browser to view the dashboard")
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
- [GitHub Repository](https://github.com/Abdullahabuzaid2021/Lightweight-web-app-for-L11-networking-BOM-aggregation---uses-repository-Excel-files)
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

### Prerequisites for Dell Team Members

#### Network Requirements
- **Must be connected to Dell internal network** (amer.dell.com domain)
- **VPN access** if working remotely
- **Dell corporate credentials** for network authentication
- **Firewall permissions** to access port 8000

#### System Requirements
- **Web browser**: Chrome, Firefox, Edge, or Safari (latest version)
- **Internet connection**: Stable connection to Dell network
- **JavaScript enabled**: Required for dashboard functionality
- **No special software installation needed**

### Access Methods

#### Method 1: Internal Dell Network (Recommended)
- **URL**: http://10.137.51.248:8000/simple_dashboard.html
- **Requirements**: Connected to Dell network or VPN
- **Best for**: Daily use, team collaboration

#### Method 2: GitHub Pages (Alternative)
- **URL**: https://abdullahabuzaid2021.github.io/Lightweight-web-app-for-L11-networking-BOM-aggregation---uses-repository-Excel-files/
- **Requirements**: Internet access (no Dell network needed)
- **Best for**: External access, sharing with non-Dell partners

### Troubleshooting Access Issues

#### Common Issues
1. **"Connection Refused"**: Server not running or network firewall blocking
2. **"Loading Data..."**: Data.json not generated or browser cache issues
3. **"404 Not Found"**: Incorrect URL path or file not found
4. **Charts Not Displaying**: Chart.js CDN blocked or JavaScript disabled

#### Solutions
1. **Test network connectivity**: `ping 10.137.51.248`
2. **Hard refresh browser**: Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac)
3. **Clear browser cache**: Clear cache and cookies
4. **Check browser console**: Press F12 to check for JavaScript errors
5. **Contact dashboard owner**: Verify server status and data processing

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