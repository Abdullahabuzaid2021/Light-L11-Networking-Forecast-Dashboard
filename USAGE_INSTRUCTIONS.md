# Usage Instructions

## Overview
This document provides step-by-step instructions on how to use and adapt the L11 Networking Forecast Dashboard solution.

## Prerequisites

### System Requirements
- **Operating System**: Windows, macOS, or Linux
- **Python**: Version 3.8 or higher
- **Web Browser**: Chrome, Firefox, Edge, or Safari (latest version)
- **Internet Connection**: Required for GitHub Pages and CDN access

### Software Requirements
- **Python Libraries**: pandas, openpyxl, flask, requests
- **Git**: For version control and GitHub integration
- **Text Editor**: VS Code, PyCharm, or similar (for code editing)

### Data Requirements
- **Excel Files**: Must contain tabs with "PnL SN6600" in their names
- **Required Columns**: Networking, Model/PN, Units
- **File Format**: .xlsx files
- **Location**: Place in data/ directory

## Installation Guide

### Step 1: Clone the Repository
```bash
# Clone the repository
git clone https://github.com/Abdullahabuzaid2021/Light-L11-Networking-Forecast-Dashboard.git
cd Light-L11-Networking-Forecast-Dashboard
```

### Step 2: Install Python Dependencies
```bash
# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Step 3: Verify Installation
```bash
# Check Python version
python --version

# Check installed packages
pip list

# Test data processing
python process_data.py
```

## Basic Usage

### Processing Data

#### Step 1: Prepare Excel Files
1. Place Excel files in the `data/` directory
2. Ensure files contain tabs with "PnL SN6600" in their names
3. Verify required columns: Networking, Model/PN, Units
4. Check file names are descriptive

#### Step 2: Run Data Processing
```bash
# Process Excel files
python process_data.py

# Expected output:
# - data.json file created
# - simple_dashboard.html updated with embedded data
# - Console summary showing processed data
```

#### Step 3: Verify Output
```bash
# Check data.json was created
ls -la data.json

# Check simple_dashboard.html was updated
# (file size should increase with embedded data)

# View data.json content (optional)
cat data.json | head -20
```

### Starting the Dashboard

#### Option 1: Flask Server with Refresh API (Recommended)
```bash
# Start Flask server on port 8000
python refresh_server.py

# Access dashboard:
# Local: http://localhost:8000/simple_dashboard.html
# Network: http://10.137.51.248:8000/simple_dashboard.html

# Refresh API: http://localhost:8000/api/refresh
```

#### Option 2: Alternative Port 8080
```bash
# Start server on port 8080
python refresh_server_8080.py

# Access dashboard:
# http://localhost:8080/simple_dashboard.html
# http://10.137.51.248:8080/simple_dashboard.html
```

#### Option 3: Simple HTTP Server (No Refresh)
```bash
# Start simple HTTP server
python start_server.py

# Access dashboard:
# http://localhost:8000/simple_dashboard.html
```

### Using the Dashboard

#### Viewing Data
1. **Summary Tab**: View all networking components
   - Shows Networking, Model/PN, and Units
   - Sorted by quantity descending
   - Search and filter functionality

2. **Files Tab**: View source file information
   - Shows file names and tab names
   - Displays item counts per file
   - Shows last modified dates

3. **Project Breakdown Tab**: View quantity distribution
   - Shows distribution across projects
   - Displays totals per project
   - Highlights overall totals

4. **Charts Tab**: View visualizations
   - Bar chart: Top 15 items by quantity
   - Pie chart: Top 10 items with percentages
   - Interactive tooltips and labels

#### Refreshing Data
1. **Add new Excel files** to data/ directory
2. **Click refresh button** in dashboard header
3. **Wait for processing** (button shows "⏳ Refreshing...")
4. **Dashboard auto-reloads** with updated data

#### Network Testing
```bash
# Test network connectivity
python network_test.py

# This will test:
# - Local server status
# - Network IP accessibility
# - Provide troubleshooting recommendations
```

## Advanced Usage

### Customizing Data Processing

#### Modifying Column Selection
```python
# Edit process_data.py
# Find this section in process_bom_data function:

# Change columns to extract
relevant_data = df[['Networking', 'Model/PN', 'Units', 'Source File', 'Source Tab', 'File Modified']].copy()

# Add or remove columns as needed
# Example: Add 'Description' column
relevant_data = df[['Networking', 'Model/PN', 'Units', 'Description', 'Source File']].copy()
```

#### Changing Aggregation Logic
```python
# Edit process_data.py
# Find the aggregation section:

# Current: Sum Units by Model/PN
summary_df = combined_df.groupby('Model/PN').agg({
    'Networking': 'first',
    'Units': 'sum'
}).reset_index()

# Example: Average instead of sum
summary_df = combined_df.groupby('Model/PN').agg({
    'Networking': 'first',
    'Units': 'mean'
}).reset_index()
```

#### Adding Data Validation
```python
# Edit process_data.py
# Add validation after data extraction:

# Example: Validate Units are positive
relevant_data = relevant_data[relevant_data['Units'] > 0]

# Example: Validate Model/PN format
relevant_data = relevant_data[relevant_data['Model/PN'].str.match(r'^[A-Z0-9\-]+$')]
```

### Customizing Dashboard

#### Changing Colors
```html
<!-- Edit simple_dashboard.html -->
<!-- Find CSS section and modify colors -->

<!-- Change gradient background -->
body {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

<!-- Change to different colors -->
body {
    background: linear-gradient(135deg, #1a73e8 0%, #00c853 100%);
}
```

#### Adding New Metrics
```html
<!-- Edit simple_dashboard.html -->
<!-- Add new metric card in HTML -->

<div class="metric-card">
    <h3>New Metric</h3>
    <div class="value" id="newMetric">-</div>
</div>

<!-- Add JavaScript to populate it -->
document.getElementById('newMetric').textContent = data.new_metric.toLocaleString();
```

#### Modifying Chart Configuration
```javascript
<!-- Edit simple_dashboard.html -->
<!-- Find chart configuration section -->

// Change bar chart colors
backgroundColor: 'rgba(102, 126, 234, 0.8)',
// Change to:
backgroundColor: 'rgba(255, 99, 132, 0.8)',

// Change chart type
type: 'bar',
// Change to:
type: 'line',
```

### GitHub Pages Deployment

#### Step 1: Configure GitHub Pages
1. Go to repository: https://github.com/Abdullahabuzaid2021/Light-L11-Networking-Forecast-Dashboard/settings/pages
2. Set **Source** to **GitHub Actions**
3. Click **Save**

#### Step 2: Push Changes
```bash
# Add new data
python process_data.py

# Commit changes
git add data.json simple_dashboard.html
git commit -m "Update dashboard data"
git push origin main
```

#### Step 3: Monitor Deployment
1. Go to **Actions** tab in repository
2. Wait for "Deploy to GitHub Pages" workflow
3. Check deployment status (should take 1-2 minutes)
4. Access dashboard at GitHub Pages URL

#### Step 4: Share URL
```
GitHub Pages URL:
https://abdullahabuzaid2021.github.io/Light-L11-Networking-Forecast-Dashboard/simple_dashboard.html
```

### Team Sharing

#### For Dell Team Members
1. **Share GitHub Pages URL** (recommended)
2. **No installation required** - just browser access
3. **Works from anywhere** - no Dell network needed
4. **Automatic updates** - when you push changes

#### For Network Access
1. **Start server**: `python refresh_server_8080.py`
2. **Share network URL**: http://10.137.51.248:8080/simple_dashboard.html
3. **Team requirements**: Dell network or VPN
4. **Firewall**: May need configuration

## Troubleshooting

### Data Processing Issues

#### Problem: "No PnL SN6600 tabs found"
**Solution**:
- Check Excel files contain tabs with "PnL SN6600" in names
- Verify files are in data/ directory
- Check file permissions

#### Problem: "Column not found"
**Solution**:
- Verify Excel files have required columns
- Check column names match exactly
- Ensure no extra spaces in column names

#### Problem: "Data processing failed"
**Solution**:
- Check Excel file formats
- Verify file sizes are reasonable
- Check for corrupted files
- Review error messages in console

### Dashboard Issues

#### Problem: Dashboard shows no data
**Solution**:
- Run `python process_data.py` to regenerate data
- Check data.json exists
- Verify data embedding in simple_dashboard.html
- Check browser console for JavaScript errors

#### Problem: Charts not displaying
**Solution**:
- Check internet connection (Chart.js requires CDN)
- Enable JavaScript in browser
- Try different browser
- Check browser console for errors

#### Problem: Refresh button not working
**Solution**:
- Ensure Flask server is running
- Check API endpoint: http://localhost:8000/api/refresh
- Verify process_data.py is accessible
- Check browser console for API errors

### Network Issues

#### Problem: Team cannot access network URL
**Solution**:
- Test local access first
- Run `python network_test.py`
- Check firewall settings
- Use GitHub Pages as alternative

#### Problem: GitHub Pages not loading
**Solution**:
- Check Actions tab for deployment status
- Verify .nojekyll file exists
- Wait 2-3 minutes for deployment
- Check repository name in URL

## Adaptation Guide

### Adapting for Different Data Sources

#### From CSV Files
```python
# Modify process_data.py to read CSV instead of Excel
import pandas as pd

# Change from:
xl = pd.ExcelFile(file_path)

# To:
df = pd.read_csv(file_path)
```

#### From Database
```python
# Add database connection
import sqlite3

# Connect to database
conn = sqlite3.connect('database.db')

# Query data
df = pd.read_sql_query("SELECT * FROM networking", conn)
```

#### From API
```python
# Add API integration
import requests

# Fetch data from API
response = requests.get('https://api.example.com/data')
data = response.json()

# Convert to DataFrame
df = pd.DataFrame(data)
```

### Adapting for Different Use Cases

#### For Inventory Management
- Add stock levels
- Add reorder points
- Add supplier information
- Create inventory alerts

#### For Cost Analysis
- Add unit costs
- Calculate total costs
- Add cost breakdown
- Create cost reports

#### For Project Planning
- Add project timelines
- Add resource allocation
- Add milestone tracking
- Create Gantt charts

## Best Practices

### Data Management
1. **Backup Excel files** before processing
2. **Version control** data.json with git
3. **Document data sources** in files table
4. **Validate data quality** regularly
5. **Archive old data** periodically

### Performance Optimization
1. **Process data in batches** for large datasets
2. **Use caching** for frequently accessed data
3. **Optimize Excel file sizes** (remove unused sheets)
4. **Monitor processing time** and optimize bottlenecks
5. **Use pagination** for large tables

### Security Considerations
1. **Don't commit sensitive data** to repository
2. **Use environment variables** for credentials
3. **Implement access control** for team sharing
4. **Regular security updates** for dependencies
5. **Audit access logs** for network deployments

### Maintenance
1. **Regular updates** to dependencies
2. **Monitor GitHub Actions** for deployment issues
3. **Keep documentation** up to date
4. **Test changes** before deployment
5. **Backup configuration** files

## Support and Resources

### Documentation
- **README.md**: Project overview and quick start
- **COMPREHENSIVE_DOCUMENTATION.md**: Complete documentation
- **DELL_TEAM_ACCESS_GUIDE.md**: Team member instructions
- **PROMPTS.md**: Development prompts and instructions
- **SAMPLE_OUTPUTS.md**: Example outputs and reports
- **DEMO_MATERIALS.md**: Demo materials and scripts
- **USAGE_INSTRUCTIONS.md**: This file

### Code Repository
- **GitHub**: https://github.com/Abdullahabuzaid2021/Light-L11-Networking-Forecast-Dashboard
- **Issues**: Report bugs and feature requests
- **Wiki**: Additional documentation and tips

### Contact Information
- **Project Owner**: Abdullah Abuzaid
- **Email**: [Your Dell email]
- **Teams**: [Your Teams contact]
- **Support**: Dell IT Help Desk for network issues

### External Resources
- **Pandas Documentation**: https://pandas.pydata.org/docs/
- **Flask Documentation**: https://flask.palletsprojects.com/
- **Chart.js Documentation**: https://www.chartjs.org/docs/
- **GitHub Pages Documentation**: https://docs.github.com/en/pages

## Quick Reference

### Common Commands
```bash
# Process data
python process_data.py

# Start server
python refresh_server.py

# Test network
python network_test.py

# Commit changes
git add .
git commit -m "Update data"
git push origin main
```

### Key URLs
- **Local Dashboard**: http://localhost:8000/simple_dashboard.html
- **Network Dashboard**: http://10.137.51.248:8000/simple_dashboard.html
- **GitHub Pages**: https://abdullahabuzaid2021.github.io/Light-L11-Networking-Forecast-Dashboard/simple_dashboard.html
- **Repository**: https://github.com/Abdullahabuzaid2021/Light-L11-Networking-Forecast-Dashboard

### File Locations
- **Excel Files**: data/ directory
- **Processed Data**: data.json
- **Dashboard**: simple_dashboard.html
- **Processing Script**: process_data.py
- **Server Script**: refresh_server.py
