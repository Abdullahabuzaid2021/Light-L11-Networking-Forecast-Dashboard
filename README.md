# L11 Networking Web App

A lightweight web application for L11 networking BOM aggregation and analysis. This approach uses Python for data processing and a static HTML/JavaScript frontend for interactive visualization, making it easy to share with team members.

## 🚀 Quick Start

### 1. Process Data
```bash
# Install dependencies
pip install -r requirements.txt

# Process Excel files and generate JSON data
python process_data.py
```

### 2. Open Dashboard
Simply open `index.html` in your web browser - no server required!

```bash
# On Windows
start index.html

# On Mac
open index.html

# On Linux
xdg-open index.html
```

## 📁 Project Structure

```
L11_Networking_Web_App/
├── data/                          # Excel files directory
│   ├── Horizon PNL.xlsx
│   ├── P&L -IREN - 50MW 252 Racks - Sweetwater VR NVL72_SN6600-LD_CORE.xlsx
│   └── P&L -IREN - 50MW 252 Racks - Sweetwater VR NVL72_SN6600-LD_DH.xlsx
├── index.html                     # Interactive dashboard (no server needed)
├── process_data.py               # Python data processing script
├── requirements.txt               # Python dependencies
├── data.json                      # Generated JSON data (after processing)
└── README.md                      # This file
```

## 🎯 Features

### Data Processing (Python)
- **Automatic File Detection**: Scans directory for Excel files with PnL SN6600 tabs
- **Data Validation**: Ensures data accuracy and consistency
- **Section Filtering**: Excludes pricing/summary tables automatically
- **Flexible Column Handling**: Works with or without Networking column
- **JSON Export**: Generates clean JSON data for web display

### Interactive Dashboard (HTML/JavaScript)
- **No Server Required**: Opens directly in any web browser
- **Real-time Search**: Filter tables by Model/PN or Networking
- **Interactive Charts**: Bar charts and pie charts using Chart.js
- **Tabbed Interface**: Summary, Files, Project Breakdown, Charts
- **Export Functionality**: Download JSON data for further analysis
- **Responsive Design**: Works on desktop and mobile devices

## 📊 Dashboard Views

### 📋 Summary Tab
- Complete BOM summary by item
- Searchable table with Networking, Model/PN, and Units
- Color-coded metrics display

### 📁 Files Tab
- Source file information
- Tab details and item counts
- File modification timestamps

### 📊 Project Breakdown Tab
- Pivot matrix showing quantities per project file
- Total column with aggregated quantities
- Networking descriptions for context

### 📈 Charts Tab
- Bar chart: Top 15 items by quantity
- Pie chart: Quantity distribution (top 10 items)
- Interactive hover effects

## 🔧 Configuration

### Data Directory
Edit `process_data.py` to change the default data directory:

```python
default_dir = r"your\custom\directory\path"
```

### Custom Data
1. Place your Excel files in the `data/` directory
2. Run `python process_data.py`
3. Open `index.html` to view the updated dashboard

## 🌐 Sharing with Team Members

### Option 1: Share Files Directly
1. Zip the entire project folder
2. Share via email, Teams, or file transfer
3. Recipients unzip and open `index.html`

### Option 2: Host on Web Server
1. Upload files to any web server (Apache, Nginx, etc.)
2. Share the URL with team members
3. No special server configuration needed

### Option 3: GitHub Pages
1. Push to GitHub repository
2. Enable GitHub Pages
3. Share the GitHub Pages URL

### Option 4: Internal SharePoint
1. Upload files to SharePoint
3. Team members can download and open `index.html`

## 🔄 Data Refresh Workflow

1. **Add/Update Excel files** in the `data/` directory
2. **Run processing script**: `python process_data.py`
3. **Refresh browser** to see updated data
4. **Share updated files** with team members if needed

## 📋 Requirements

### For Data Processing
- Python 3.7+
- pandas
- openpyxl

### For Dashboard Viewing
- Any modern web browser (Chrome, Firefox, Edge, Safari)
- No additional software required

## 🎨 Customization

### Styling
Edit the CSS in `index.html` to customize:
- Colors and gradients
- Layout and spacing
- Font styles
- Chart colors

### Functionality
Edit the JavaScript in `index.html` to:
- Add new chart types
- Modify search logic
- Add export formats
- Customize table displays

## 🔒 Security

- **No Server Required**: Reduces security concerns
- **Local Processing**: Data stays on your machine
- **No External Dependencies**: Uses CDN for Chart.js only
- **Static Files**: No database or backend required

## 📈 Advantages Over Streamlit Approach

1. **Easier Sharing**: No server setup required
2. **Universal Access**: Opens in any browser
3. **Lightweight**: Minimal dependencies
4. **Offline Capable**: Works without internet (except Chart.js CDN)
5. **Simple Deployment**: Can be hosted anywhere
6. **Team Friendly**: Easy for non-technical users

## 🚀 Future Enhancements

- Add more chart types and visualizations
- Implement data filtering by date ranges
- Add comparison views between different time periods
- Include quarterly forecasting analysis
- Add authentication for sensitive data
- Implement real-time data updates

## 📞 Support

For issues or questions, contact the development team.

## 📱 Quick Links

- **Dashboard**: Open `index.html` in your browser
- **Data Processing**: Run `python process_data.py`
- **Sample Data**: Included in `data/` directory
- **SharePoint Source**: [Hackathon - L11 forecasting](https://dell.sharepoint.com/:f:/r/sites/NetworkingL11RackPlanning/Shared%20Documents/General/Hackathon%20-%20L11%20forecasting?d=wb9ae5c4571d84bec94d375ef7ea58856&csf=1&web=1&e=KNnpRl)
