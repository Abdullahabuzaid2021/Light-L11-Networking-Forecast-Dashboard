#!/usr/bin/env python3
"""
Flask server for L11 Networking Dashboard with refresh API
Uses port 80 (standard HTTP port) which is often open by default
"""

from flask import Flask, jsonify, send_from_directory
from pathlib import Path
import subprocess
import json
from datetime import datetime

app = Flask(__name__)

# Get the directory where this script is located
BASE_DIR = Path(__file__).parent.parent.parent.resolve()

def process_data():
    """Run the data processing script"""
    try:
        result = subprocess.run(
            ['python', 'process_data.py'],
            cwd=BASE_DIR / 'documentation' / 'code_scripts',
            capture_output=True,
            text=True,
            timeout=60
        )
        
        # Check if data.json was created/updated
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
    return send_from_directory(BASE_DIR / 'dashboard', 'simple_dashboard.html')

@app.route('/dashboard/')
def serve_dashboard_folder():
    """Serve the dashboard folder"""
    return send_from_directory(BASE_DIR / 'dashboard', 'index.html')

@app.route('/dashboard/simple_dashboard.html')
def serve_dashboard():
    """Serve the dashboard"""
    return send_from_directory(BASE_DIR / 'dashboard', 'simple_dashboard.html')

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
    PORT = 80  # Standard HTTP port
    
    print("=" * 60)
    print("L11 Networking Dashboard Server (Port 80)")
    print("=" * 60)
    print(f"Server directory: {BASE_DIR}")
    print(f"Dashboard URL: http://localhost/dashboard/simple_dashboard.html")
    print(f"Network URL: http://10.137.51.248/dashboard/simple_dashboard.html")
    print(f"Refresh API: http://localhost/api/refresh")
    print("=" * 60)
    print("NOTE: Port 80 might be blocked by another service")
    print("If port 80 is in use, try port 8080 or use GitLab Pages")
    print("=" * 60)
    print("Press Ctrl+C to stop the server")
    print("=" * 60)
    
    try:
        # Run the server on all interfaces for network access
        app.run(host='0.0.0.0', port=PORT, debug=False)
    except PermissionError:
        print("\nERROR: Port 80 requires admin rights or is already in use")
        print("Please try:")
        print("1. python refresh_server_8080.py (port 8080)")
        print("2. Use GitLab Pages instead")
        print("3. Contact IT to deploy to internal web server")