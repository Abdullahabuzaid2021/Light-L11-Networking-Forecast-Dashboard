# L11 Networking Web App

A lightweight web application for L11 networking BOM aggregation and analysis. This approach uses Python for data processing and a static HTML/JavaScript frontend for interactive visualization, making it easy to share with team members.

## 🚀 Quick Access

**Dashboard URL**: http://localhost:8000/simple_dashboard.html (when running Flask server)

**Dell Internal Network URLs** (for team sharing):
- **Network URL**: http://10.137.51.248:8000/simple_dashboard.html (within Dell network) - **Primary for team sharing**
- **External URL**: http://143.166.192.16:8000/simple_dashboard.html (if accessible) - **Alternative for broader access**

**GitHub Repository**: https://github.com/Abdullahabuzaid2021/Lightweight-web-app-for-L11-networking-BOM-aggregation---uses-repository-Excel-files

**SharePoint Data Source**: [Hackathon - L11 forecasting](https://dell.sharepoint.com/:f:/r/sites/NetworkingL11RackPlanning/Shared%20Documents/General/Hackathon%20-%20L11%20forecasting?d=wb9ae5c4571d84bec94d375ef7ea58856&csf=1&web=1&e=rBs2jB)

**Server Type**: Flask server with refresh API (recommended)

## 📚 Documentation

- **[Comprehensive Documentation](COMPREHENSIVE_DOCUMENTATION.md)** - Complete guide with prompts, sample outputs, and code scripts
- **[Dell Team Access Guide](DELL_TEAM_ACCESS_GUIDE.md)** - Step-by-step guide for Dell team members to access the dashboard
- **[Network Testing Script](network_test.py)** - Automated tool to test network connectivity and server accessibility

## Problem Statement

The L11 networking team faces a significant challenge in aggregating Bill of Materials (BOM) data from multiple individual project files. Each project maintains its own Excel file with networking component data in PnL SN6600 tabs, making it difficult to:

- **Consolidate Data**: Aggregate quantities across multiple projects to get total networking requirements
- **Ensure Data Accuracy**: Validate that data from different sources is consistent and usable before analysis
- **Real-time Monitoring**: Track changes and new additions across multiple project files
- **Strategic Planning**: Make informed decisions based on comprehensive networking component forecasts

The manual process of combining data from numerous Excel files is time-consuming, error-prone, and doesn't provide the real-time visibility needed for effective planning and forecasting.

## Plan Function

To address these challenges, we developed an automated solution with the following approach:

1. **Automated Data Aggregation**: Create a system that automatically processes all Excel files in a designated directory
2. **Data Validation**: Implement robust data validation to ensure accuracy and consistency before use
3. **Interactive Dashboard**: Build a user-friendly interface for querying, visualizing, and exporting the aggregated data
4. **Real-time Updates**: Enable automatic detection of new files and data refresh capabilities
5. **Internal Collaboration**: Design the system for easy sharing within Dell's internal environment

## Solution Steps Breakdown

### Phase 1: Data Processing Engine
- **File Detection**: Implemented automatic scanning of directories for Excel files with PnL SN6600 tabs
- **Data Extraction**: Created robust parsing logic to handle varying Excel file structures
- **Data Validation**: Added validation to ensure data accuracy:
  - Required column checks (Model/PN, Units)
  - Optional column handling (Networking)
  - Zero-value filtering
  - Section detection to exclude pricing/summary tables
- **Data Aggregation**: Developed logic to combine data from multiple files and sum quantities by Model/PN
- **JSON Generation**: Created clean JSON output for web display

### Phase 2: Dashboard Development
- **User Interface**: Built HTML/JavaScript-based dashboard with intuitive navigation
- **Data Visualization**: Implemented interactive charts (bar charts, pie charts) with value labels
- **Query Capabilities**: Added search and filtering functionality for specific item analysis
- **Export Features**: Enabled JSON export for reporting and sharing

### Phase 3: Advanced Features
- **Project File Breakdown**: Created pivot matrix showing quantities per project file
- **Quantity Analysis**: Added statistical analysis (min, max, median, standard deviation)
- **New File Detection**: Implemented visual indicators for new files added to the directory
- **Auto-Refresh**: Added optional automatic data refresh functionality

### Phase 4: Deployment & Sharing
- **Internal Sharing**: Configured for Dell internal network access via local server
- **Source Control**: Managed code through GitHub for collaboration
- **Documentation**: Created comprehensive setup and usage documentation
- **Scalability**: Designed for easy deployment on web servers or GitHub Pages

## Conclusion of Outcome

The L11 Networking Web App successfully addresses the original problem statement by providing:

### ✅ Key Achievements
- **Automated Aggregation**: Processes multiple Excel files automatically, eliminating manual consolidation
- **Data Accuracy**: Implements robust validation to ensure only accurate, usable data is included
- **Real-time Visibility**: Provides immediate visibility into total networking requirements across all projects
- **Interactive Analysis**: Enables detailed querying and filtering of component data
- **Strategic Insights**: Supports better planning through comprehensive data visualization and export capabilities

### 📊 Measurable Results
- **Processing Efficiency**: Reduces data consolidation time from hours to seconds
- **Data Accuracy**: Eliminates manual errors through automated validation
- **Coverage**: Successfully processes diverse Excel file structures with flexible column handling
- **User Adoption**: Intuitive interface enables quick adoption by team members
- **Scalability**: Designed to handle growing numbers of projects and files

### 🎯 Business Impact
- **Improved Planning**: Better forecasting accuracy for networking component requirements
- **Cost Optimization**: Enhanced visibility enables better procurement decisions
- **Time Savings**: Significant reduction in manual data processing time
- **Error Reduction**: Automated validation eliminates manual consolidation errors
- **Collaboration**: Enables team-wide access to consistent, up-to-date BOM data

The web app has transformed a manual, error-prone process into an automated, reliable system that provides real-time insights for L11 networking planning and decision-making.

## Features

1. **Automatic File Detection**: Monitors the specified directory for new Excel files
2. **BOM Aggregation**: Automatically aggregates BOM data from all PnL SN6600 tabs across multiple Excel files
3. **Interactive Dashboard**: 
   - Table view with complete BOM summary
   - Bar charts and pie charts with value labels for data visualization
   - Key metrics (total items, quantities, files, tabs)
4. **Query Capabilities**:
   - Search by Model/PN or Networking description
   - Filter by quantity ranges
   - Show top N items
5. **Export Functionality**:
   - Export complete summary to JSON
   - Export query results to JSON
6. **Auto-Refresh**: Optional 30-second auto-refresh for real-time monitoring
7. **Internal Sharing**: Designed for easy sharing within Dell

## Installation

1. Install required dependencies:
```bash
pip install -r requirements.txt
```

2. Process the data:
```bash
python process_data.py
```

3. Run the dashboard with Flask server (recommended):
```bash
python refresh_server.py
```

Alternative: Run with simple HTTP server:
```bash
python start_server.py
```

## Dashboard Access

### 🌐 Dell Internal Sharing (Recommended for Team Access)
The dashboard can be shared with other Dell members via the network URLs:
- **Network URL**: http://10.137.51.248:8000/simple_dashboard.html (within Dell network) - **Primary for team sharing**
- **External URL**: http://143.166.192.16:8000/simple_dashboard.html (if accessible) - **Alternative for broader access**

**How to Share:**
1. Run the dashboard on your machine: `python start_server.py`
2. Share the Network URL (http://10.137.51.248:8000/simple_dashboard.html) with your team
3. Team members can access it directly within the Dell network
4. No additional server setup required
5. **See [Dell Team Access Guide](DELL_TEAM_ACCESS_GUIDE.md)** for detailed team member instructions

### Local Development
When running locally, the dashboard is accessible at:
- **Local URL**: http://localhost:8000/simple_dashboard.html (only on your machine)
- **Network URL**: http://10.137.51.248:8000/simple_dashboard.html (within Dell network)
- **External URL**: http://143.166.192.16:8000/simple_dashboard.html (if accessible)

### Deployment Options
The dashboard can be deployed for team access through:

**Web Server** (Recommended for sharing):
- Deploy on any web server (Apache, Nginx, etc.)
- Upload files and share the URL
- No special server configuration needed

**GitHub Pages**:
- Deploy via GitHub repository
- Get a permanent URL like `https://abdullahabuzaid2021.github.io/Lightweight-web-app-for-L11-networking-BOM-aggregation---uses-repository-Excel-files/`
- Easy sharing with team members

**Internal Server**:
- Deploy on Dell internal servers
- Configure for intranet access
- Suitable for sensitive data

### Quick Start
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Process data: `python process_data.py`
4. Run dashboard: `python refresh_server.py` (recommended) or `python start_server.py` (alternative)
5. Access at http://localhost:8000/simple_dashboard.html

## Configuration

- **Default Directory**: `data/` (included in repository with sample files)
- **Alternative Directory**: `C:\Users\Abdullah_Abuzaid\OneDrive - Dell Technologies\Desktop\Hackathon exercise`
- **SharePoint Location**: [Hackathon - L11 forecasting](https://dell.sharepoint.com/:f:/r/sites/NetworkingL11RackPlanning/Shared%20Documents/General/Hackathon%20-%20L11%20forecasting?d=wb9ae5c4571d84bec94d375ef7ea58856&csf=1&web=1&e=rBs2jB)
- **Supported File Format**: Excel files (.xlsx) with tabs containing "PnL SN6600" in the name
- **Required Columns**: Networking, Model/PN, Units
- **Dashboard URL**: http://localhost:8000 (when running local server)

### Sample Data Included

The repository includes sample Excel files in the `data/` directory:
- `Horizon PNL.xlsx` - Sample Horizon project BOM data
- `P&L -IREN - 50MW 252 Racks - Sweetwater VR NVL72_SN6600-LD_CORE.xlsx` - CORE project data
- `P&L -IREN - 50MW 252 Racks - Sweetwater VR NVL72_SN6600-LD_DH.xlsx` - DH project data

These files can be used immediately to test the dashboard functionality.

### Data Directory Structure

```
L11_Networking_Web_App/
├── data/
│   ├── Horizon PNL.xlsx
│   ├── P&L -IREN - 50MW 252 Racks - Sweetwater VR NVL72_SN6600-LD_CORE.xlsx
│   ├── P&L -IREN - 50MW 252 Racks - Sweetwater VR NVL72_SN6600-LD_DH.xlsx
│   └── total summary BOM per item.xlsx
├── simple_dashboard.html (RECOMMENDED - simplified dashboard)
├── index.html (original complex dashboard)
├── process_data.py
├── start_server.py
├── network_test.py (network connectivity testing)
├── requirements.txt
├── data.json
├── README.md
├── COMPREHENSIVE_DOCUMENTATION.md
└── DELL_TEAM_ACCESS_GUIDE.md
```

### SharePoint Integration

The dashboard is designed to work with locally synced SharePoint folders. To use the SharePoint location:

1. **Sync SharePoint Folder**: Use OneDrive or SharePoint sync client to sync the folder locally
2. **Use Local Path**: Configure the dashboard to use the local synced folder path
3. **Automatic Updates**: Changes in SharePoint will sync to the local folder and be detected by the dashboard

**Note**: Direct SharePoint API integration requires additional authentication setup. The current implementation uses local file system access for simplicity and security.

## Usage

1. **Process Data**: Run `python process_data.py` to process Excel files and generate JSON
2. **Start Dashboard**: Run `python refresh_server.py` to start the Flask server with refresh API
3. **Test Network**: Run `python network_test.py` to verify network connectivity for team sharing
4. **Access Dashboard**: Open http://localhost:8000/simple_dashboard.html in your browser
5. **Refresh Data**: Click the "🔄 Refresh Data" button to process new Excel files
6. **Navigate Tabs**: Use Summary, Files, Project Breakdown, and Charts tabs
7. **Visualize Data**: View interactive charts with value labels
8. **Share with Team**: Share network URL with Dell team members (see Dell Team Access Guide)

## Deployment Options for Internal Sharing

### Option 1: Flask Server with Refresh API (Recommended for Dell)
1. Run: `python refresh_server.py`
2. Test network: `python network_test.py`
3. Share the network URL: http://10.137.51.248:8000/simple_dashboard.html
4. Team members can refresh data by clicking the refresh button
5. No additional setup required
6. **See [Dell Team Access Guide](DELL_TEAM_ACCESS_GUIDE.md)** for team instructions

### Option 2: Simple HTTP Server
1. Run: `python start_server.py`
2. Share the network URL: http://10.137.51.248:8000/simple_dashboard.html
3. Team members access via Dell network
4. Note: No refresh functionality with this option

### Option 3: Web Server
1. Upload files to any web server
2. Share the server URL
3. No special configuration needed

### Option 4: GitHub Pages
1. Push code to GitHub repository
2. Enable GitHub Pages
3. Share the GitHub Pages URL
4. Automatic deployment on push

## Future Enhancements

- Quarterly forecast analysis
- Delivery schedule parsing
- Trend analysis and forecasting
- Quarter-over-quarter comparisons
- Demand planning metrics
- Authentication and access control
- Additional chart types and visualizations
- Data filtering by date ranges
- Comparison views between different time periods

## Technical Details

- **Frontend**: HTML, CSS, JavaScript
- **Data Processing**: Python with Pandas
- **Visualization**: Chart.js with datalabels plugin
- **File Processing**: OpenPyXL
- **Server**: Python HTTP server
- **Network Testing**: Requests library for connectivity testing

## Support

For issues or questions, contact the development team.

## 📱 Dashboard Links

### Local Access
- **Primary URL**: http://localhost:8000/simple_dashboard.html (RECOMMENDED)
- **Network URL**: http://10.137.51.248:8000/simple_dashboard.html (Dell internal network)
- **External URL**: http://143.166.192.16:8000/simple_dashboard.html (if accessible)

### Repository & Resources
- **GitHub Repository**: https://github.com/Abdullahabuzaid2021/Lightweight-web-app-for-L11-networking-BOM-aggregation---uses-repository-Excel-files
- **SharePoint Data**: [Hackathon - L11 forecasting](https://dell.sharepoint.com/:f:/r/sites/NetworkingL11RackPlanning/Shared%20Documents/General/Hackathon%20-%20L11%20forecasting?d=wb9ae5c4571d84bec94d375ef7ea58856&csf=1&web=1&e=rBs2jB)
- **Comprehensive Documentation**: [COMPREHENSIVE_DOCUMENTATION.md](COMPREHENSIVE_DOCUMENTATION.md)
- **Dell Team Access Guide**: [DELL_TEAM_ACCESS_GUIDE.md](DELL_TEAM_ACCESS_GUIDE.md)

### Quick Start Commands
```bash
# Clone the repository
git clone https://github.com/Abdullahabuzaid2021/Lightweight-web-app-for-L11-networking-BOM-aggregation---uses-repository-Excel-files.git
cd Lightweight-web-app-for-L11-networking-BOM-aggregation---uses-repository-Excel-files

# Install dependencies
pip install -r requirements.txt

# Process data
python process_data.py

# Test network connectivity (for team sharing)
python network_test.py

# Run the dashboard (recommended - with refresh functionality)
python refresh_server.py

# Alternative: Simple HTTP server (no refresh)
python start_server.py

# Access the dashboard
# Open http://localhost:8000/simple_dashboard.html in your browser
```

## 🆕 New Features

### Enhanced Dashboard (simple_dashboard.html)
- **Simplified Architecture**: Data embedded directly in HTML for immediate loading
- **Value Labels**: Charts now display values directly on chart elements
- **Project Breakdown Tab**: Per-project quantity distribution with totals
- **Improved Performance**: Faster loading with embedded data
- **Better Error Handling**: Enhanced logging and debugging capabilities

### Flask Server with Refresh API (refresh_server.py)
- **Refresh Button**: One-click data refresh functionality
- **API Endpoint**: POST `/api/refresh` for triggering data processing
- **Network Access**: Configured for Dell internal network sharing
- **Automatic Updates**: Dashboard auto-reloads after successful refresh
- **Error Handling**: Comprehensive error messages and user feedback

### Network Testing (network_test.py)
- **Automated Connectivity Testing**: Tests local server, network IP, and data files
- **Firewall Diagnostics**: Checks port accessibility and network configuration
- **Comprehensive Reporting**: Generates detailed access reports for troubleshooting
- **Dell Network Validation**: Verifies Dell network connectivity for team sharing

### Documentation
- **Comprehensive Documentation**: Complete guide with prompts, sample outputs, and code scripts
- **Dell Team Access Guide**: Step-by-step instructions for Dell team members
- **Troubleshooting Procedures**: Common issues and solutions for network access
- **Best Practices**: Security considerations and usage guidelines
