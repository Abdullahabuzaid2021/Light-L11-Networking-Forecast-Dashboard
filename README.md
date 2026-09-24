# L11 Networking Forecast Dashboard

A lightweight web application for L11 networking BOM aggregation and analysis.

## 🌐 Dashboard Access (RECOMMENDED - No Admin Rights Required)

**GitLab Pages URL**: https://abdullah-abuzaid.gitlab.io/light-l11-networking-forecast-dashboard/simple_dashboard.html

**Benefits:**
- ✅ No admin rights required
- ✅ Works globally without Dell network
- ✅ No firewall configuration needed
- ✅ Permanent URL always available
- ✅ Best for team sharing

---

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
├── .nojekyll                       # Disables Jekyll for GitLab Pages
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
- **GitLab Pages (RECOMMENDED)**: https://abdullah-abuzaid.gitlab.io/light-l11-networking-forecast-dashboard/simple_dashboard.html
- **Local**: http://localhost:8000/dashboard/simple_dashboard.html
- **Dell Network**: http://10.137.51.248:8000/dashboard/simple_dashboard.html (requires firewall configuration)
- **Alternative Port**: http://10.137.51.248:8080/dashboard/simple_dashboard.html

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
- **Dell Network Sharing**: Internal network access for team members
- **Multiple Server Options**: Port 8000, 8080, and 80 available

## 📊 Data Files

Excel files in `data/` directory:
- HOZN PNL.xlsx
- P&L -I - 50MW 252 Racks - STWR VR NVL72_SN6600-LD_CORE.xlsx
- P&L -I - 50MW 252 Racks - STWR VR NVL72_SN6600-LD_DH.xlsx
- total summary BOM per item.xlsx

## 🔧 Automation Level: ACCELERATED

This solution significantly speeds up BOM aggregation (99.9% time reduction) while maintaining human oversight for data validation and strategic decision-making.

## 📱 Dashboard Links

- **GitLab Pages (RECOMMENDED)**: https://abdullah-abuzaid.gitlab.io/light-l11-networking-forecast-dashboard/simple_dashboard.html
- **GitLab Repository**: https://eos2git.cec.lab.emc.com/Abdullah-Abuzaid/Light-L11-Networking-Forecast-Dashboard
- **Local Access**: http://localhost:8000/dashboard/simple_dashboard.html
- **Dell Network Access**: http://10.137.51.248:8000/dashboard/simple_dashboard.html (requires firewall configuration)

## 🤝 Support

For detailed documentation, see the `documentation/` folder. Each section contains comprehensive guides for understanding, using, and adapting the solution.
