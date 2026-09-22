# L11 Networking Web App

A lightweight web application for L11 networking BOM aggregation and analysis. This approach uses Python for data processing and a static HTML/JavaScript frontend for interactive visualization, making it easy to share with team members.

## 🚀 Quick Access

- **GitHub Repository**: https://github.com/Abdullahabuzaid2021/Lightweight-web-app-for-L11-networking-BOM-aggregation---uses-repository-Excel-files
- **GitHub Pages Dashboard**: https://abdullahabuzaid2021.github.io/Lightweight-web-app-for-L11-networking-BOM-aggregation---uses-repository-Excel-files/ (after enabling GitHub Pages)
- **Local Dashboard**: Open `index.html` in your browser
- **Data Processing**: Run `python process_data.py`
- **Data Source**: Excel files in repository `data/` directory
- **SharePoint Reference**: [Hackathon - L11 forecasting](https://dell.sharepoint.com/:f:/r/sites/NetworkingL11RackPlanning/Shared%20Documents/General/Hackathon%20-%20L11%20forecasting?d=wb9ae5c4571d84bec94d375ef7ea58856&csf=1&web=1&e=rBs2jB)

## 🚀 Quick Start

### 1. Process Data
```bash
# Install dependencies
pip install -r requirements.txt

# Process Excel files from repository and generate JSON
python process_data.py
```

**Data Source:**
- Uses Excel files directly from the repository `data/` directory
- No external dependencies or sync required
- Simple and reliable approach

### 2. Open Dashboard
**Option A: Using Local Server (Recommended)**
```bash
# Start the local server
python start_server.py

# The dashboard will open automatically in your browser
# Or manually open: http://localhost:8000/index.html
```

**Option B: Direct File Opening**
```bash
# On Windows
start index.html

# On Mac
open index.html

# On Linux
xdg-open index.html
```

**Note**: If you see "Error loading data" when opening directly, use the local server option instead.

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
- **Primary**: Uses Excel files from repository `data/` directory
- **No external configuration required**
- **Simple and reliable**

### Custom Data
1. Place your Excel files in the `data/` directory
2. Run `python process_data.py`
3. Open `index.html` to view the updated dashboard

## 🌐 Team Sharing & Dashboard Link

### **GitHub Pages Dashboard Link (Primary)**
**Dashboard URL**: https://abdullahabuzaid2021.github.io/Lightweight-web-app-for-L11-networking-BOM-aggregation---uses-repository-Excel-files/

**To enable GitHub Pages:**
1. Go to repository Settings → Pages
2. Select "GitHub Actions" as Source
3. Click Save
4. Wait for automatic deployment (2-3 minutes)
5. Share the above URL with your team

**Benefits of GitHub Pages:**
- Permanent shareable link
- Automatic updates when you push code
- No server setup required
- Works for all team members

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

### Update Excel Files in Repository
1. **Add/Update Excel files** in the `data/` directory
2. **Run processing script**: `python process_data.py`
3. **Refresh browser** to see updated data
4. **Commit changes** to git repository (optional)

### Team Sharing
- Share the entire project folder via git repository
- Team members clone the repository
- Excel files are included in the repository
- Each user runs `python process_data.py` to process the data

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
