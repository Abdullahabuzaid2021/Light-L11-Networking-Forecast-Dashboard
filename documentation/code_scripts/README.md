# Code Scripts - Automation Scripts

This section contains the automation scripts and code that power the L11 Networking Forecast Dashboard solution.

## Files in This Section

- **[process_data.py](process_data.py)** - Main data processing script that:
  - Processes Excel files from data/ directory
  - Extracts data from PnL SN6600 tabs
  - Aggregates BOM data by Model/PN
  - Creates pivot tables for project breakdown
  - Generates JSON output for dashboard
  - Embeds data in HTML for GitHub Pages

- **[refresh_server.py](refresh_server.py)** - Flask server with refresh API that:
  - Serves dashboard files
  - Provides API endpoint for data refresh
  - Allows one-click data refresh without server restart
  - Runs on port 8000

- **[refresh_server_8080.py](refresh_server_8080.py)** - Alternative server on port 8080

- **[refresh_server_80.py](refresh_server_80.py)** - Alternative server on port 80

- **[start_server.py](start_server.py)** - Simple HTTP server (no refresh functionality)

- **[network_test.py](network_test.py)** - Network connectivity testing script that:
  - Tests local server status
  - Tests network IP accessibility
  - Provides troubleshooting recommendations

## Quick Reference

To run the data processing script:
```bash
cd documentation/code_scripts
python process_data.py
```

To start the Flask server:
```bash
cd documentation/code_scripts
python refresh_server.py
```

To test network connectivity:
```bash
cd documentation/code_scripts
python network_test.py
```

## Related Documentation

- **[README](../readme/)** - Project overview
- **[Prompts](../prompts/)** - Development prompts
- **[Sample Outputs](../sample_outputs/)** - Example outputs
- **[Demo Materials](../demo_materials/)** - Screenshots and presentations
- **[Usage Instructions](../usage_instructions/)** - Step-by-step guide
