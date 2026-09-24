# L11 Networking Forecast Dashboard

A lightweight web application for L11 networking BOM aggregation and analysis.

## 📁 Repository Structure

```
Light-L11-Networking-Forecast-Dashboard/
├── documentation/                   # All documentation organized by category
│   ├── readme/                     # README and project overview
│   ├── prompts/                    # Development prompts and instructions
│   ├── sample_outputs/             # Example outputs and reports
│   ├── demo_materials/             # Screenshots, videos, and presentations
│   ├── code_scripts/               # Automation scripts and code
│   └── usage_instructions/         # Step-by-step usage guide
├── dashboard/                      # Dashboard files
│   ├── simple_dashboard.html       # Main dashboard (with embedded data)
│   └── index.html                  # Alternative dashboard
├── data/                           # Excel files directory
├── data.json                       # Generated data file
├── .nojekyll                       # Disables Jekyll for GitHub Pages
└── README.md                       # Main project README
```

## 🚀 Quick Start

### 1. Process Data
```bash
cd documentation/code_scripts
python process_data.py
```

### 2. Start Server
```bash
cd documentation/code_scripts
python refresh_server.py
```

### 3. Access Dashboard
- **Local**: http://localhost:8000/dashboard/simple_dashboard.html
- **GitHub Pages**: https://abdullahabuzaid2021.github.io/Light-L11-Networking-Forecast-Dashboard/simple_dashboard.html

## 📚 Documentation

- **[README](documentation/readme/README.md)** - Project overview and approach
- **[Prompts](documentation/prompts/PROMPTS.md)** - Development prompts and templates
- **[Sample Outputs](documentation/sample_outputs/SAMPLE_OUTPUTS.md)** - Example outputs and reports
- **[Demo Materials](documentation/demo_materials/DEMO_MATERIALS.md)** - Screenshots and presentations
- **[Code Scripts](documentation/code_scripts/)** - Automation scripts
- **[Usage Instructions](documentation/usage_instructions/USAGE_INSTRUCTIONS.md)** - Step-by-step guide

## 🎯 Key Features

- **Automated Data Processing**: Processes Excel files with PnL SN6600 tabs
- **Interactive Dashboard**: Web-based visualization with charts and tables
- **One-Click Refresh**: Update data without server restart
- **Team Sharing**: GitHub Pages for global access
- **No Admin Rights Required**: Works without firewall configuration

## 📊 Data Files

Excel files in `data/` directory:
- HOZN PNL.xlsx
- P&L -I - 50MW 252 Racks - STWR VR NVL72_SN6600-LD_CORE.xlsx
- P&L -I - 50MW 252 Racks - STWR VR NVL72_SN6600-LD_DH.xlsx
- total summary BOM per item.xlsx

## 🔧 Automation Level: ACCELERATED

This solution significantly speeds up BOM aggregation (99.9% time reduction) while maintaining human oversight for data validation and strategic decision-making.

## 📱 Dashboard Links

- **GitHub Pages**: https://abdullahabuzaid2021.github.io/Light-L11-Networking-Forecast-Dashboard/simple_dashboard.html
- **Repository**: https://github.com/Abdullahabuzaid2021/Light-L11-Networking-Forecast-Dashboard

## 🤝 Support

For detailed documentation, see the `documentation/` folder. Each section contains comprehensive guides for understanding, using, and adapting the solution.
