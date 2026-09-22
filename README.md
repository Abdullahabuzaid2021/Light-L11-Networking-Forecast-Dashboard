# L11 Networking Web App

A lightweight web application for L11 networking BOM aggregation and analysis. This approach uses Python for data processing and a static HTML/JavaScript frontend for interactive visualization, making it easy to share with team members.

## 🚀 Quick Access

- **SharePoint Data Source**: [Hackathon - L11 forecasting](https://dell.sharepoint.com/:f:/r/sites/NetworkingL11RackPlanning/Shared%20Documents/General/Hackathon%20-%20L11%20forecasting?d=wb9ae5c4571d84bec94d375ef7ea58856&csf=1&web=1&e=rBs2jB)
- **Local Dashboard**: Open `index.html` in your browser
- **Data Processing**: Run `python process_data.py`

## 🚀 Quick Start

### 1. Process Data (with SharePoint Sync)
```bash
# Install dependencies
pip install -r requirements.txt

# Process Excel files - automatically syncs from SharePoint and generates JSON
python process_data.py
```

**SharePoint Integration:**
- The script automatically syncs Excel files from your SharePoint-synced directory
- Default SharePoint path: `C:\Users\Abdullah_Abuzaid\OneDrive - Dell Technologies\Desktop\Hackathon exercise`
- Update the `sharepoint_dir` variable in `process_data.py` if your sync location is different
- Falls back to local data directory if SharePoint sync fails

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

### SharePoint Sync Setup
The script automatically syncs files from SharePoint. To configure:

1. **Sync SharePoint Folder Locally:**
   - Use OneDrive or SharePoint sync client
   - Sync the "Hackathon - L11 forecasting" folder to your local machine
   - Note the local sync path

2. **Update SharePoint Path:**
   Edit `process_data.py` and update the `sharepoint_dir` variable:
   ```python
   sharepoint_dir = r"your\local\sharepoint\sync\path"
   ```

3. **Run Processing:**
   ```bash
   python process_data.py
   ```
   The script will automatically sync files from SharePoint and process them.

### Data Directory
- **Primary**: Uses SharePoint-synced files (if configured)
- **Fallback**: Uses local `data/` directory if SharePoint sync fails
- **Manual**: Place Excel files directly in `data/` directory

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

### Automatic SharePoint Sync
1. **Update files in SharePoint** (via web interface or sync client)
2. **Run processing script**: `python process_data.py`
3. **Script automatically syncs** latest files from SharePoint
4. **Refresh browser** to see updated data

### Manual Data Update
1. **Add/Update Excel files** in the `data/` directory
2. **Run processing script**: `python process_data.py`
3. **Refresh browser** to see updated data
4. **Share updated files** with team members if needed

### Team Sharing
- Share the entire project folder (including synced data)
- Team members run `python process_data.py` to sync and process
- Each user can configure their own SharePoint sync path

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
