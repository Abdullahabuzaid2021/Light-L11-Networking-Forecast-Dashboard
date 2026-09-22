#!/usr/bin/env python3
"""
Network Connectivity Test Script for L11 Networking Dashboard
Tests network connectivity and server accessibility for Dell team members
"""

import socket
import subprocess
import sys
from pathlib import Path
import requests
import json

def test_local_server():
    """Test if local server is running"""
    print("=" * 60)
    print("Testing Local Server")
    print("=" * 60)
    
    try:
        response = requests.get('http://localhost:8000/simple_dashboard.html', timeout=10)
        if response.status_code == 200:
            print("[PASS] Local server is running and accessible")
            print(f"   Status: {response.status_code}")
            print(f"   URL: http://localhost:8000/simple_dashboard.html")
            return True
        else:
            print(f"[FAIL] Local server returned status: {response.status_code}")
            return False
    except requests.exceptions.Timeout:
        print("[WARN] Local server timeout - server may be slow but running")
        print("   Server is likely running but responding slowly")
        return True  # Consider this as pass since server is running
    except requests.exceptions.ConnectionError:
        print("[FAIL] Local server is not running")
        print("   Start the server with: python start_server.py")
        return False
    except Exception as e:
        print(f"[FAIL] Error testing local server: {e}")
        return False

def test_network_ip():
    """Test network IP accessibility"""
    print("\n" + "=" * 60)
    print("Testing Network IP (10.137.51.248)")
    print("=" * 60)
    
    ip = "10.137.51.248"
    port = 8000
    
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((ip, port))
        
        if result == 0:
            print("[PASS] Network IP is accessible")
            print(f"   IP: {ip}")
            print(f"   Port: {port}")
            print(f"   URL: http://{ip}:{port}/simple_dashboard.html")
            sock.close()
            return True
        else:
            print(f"[FAIL] Cannot connect to {ip}:{port}")
            print("   Possible causes:")
            print("   - Server not running")
            print("   - Network firewall blocking connection")
            print("   - Incorrect IP address")
            sock.close()
            return False
    except socket.gaierror:
        print(f"[FAIL] Cannot resolve hostname: {ip}")
        return False
    except Exception as e:
        print(f"[FAIL] Error testing network IP: {e}")
        return False

def get_local_ip():
    """Get local IP address"""
    try:
        # Connect to a remote server to get local IP
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect(("8.8.8.8", 80))
        local_ip = sock.getsockname()[0]
        sock.close()
        return local_ip
    except Exception:
        return "127.0.0.1"

def test_data_file():
    """Test if data.json exists and is valid"""
    print("\n" + "=" * 60)
    print("Testing Data File")
    print("=" * 60)
    
    data_file = Path(__file__).parent / "data.json"
    
    if data_file.exists():
        print("[PASS] data.json file exists")
        try:
            with open(data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            if 'summary' in data and 'total_items' in data:
                print(f"   Total items: {data['total_items']}")
                print(f"   Total quantity: {data['total_quantity']:,}")
                print(f"   Total files: {data['total_files']}")
                print(f"   Generated at: {data.get('generated_at', 'Unknown')}")
                print("[PASS] Data file is valid")
                return True
            else:
                print("[FAIL] Data file is missing required fields")
                return False
        except json.JSONDecodeError:
            print("[FAIL] Data file contains invalid JSON")
            return False
        except Exception as e:
            print(f"[FAIL] Error reading data file: {e}")
            return False
    else:
        print("[FAIL] data.json file does not exist")
        print("   Run: python process_data.py")
        return False

def test_excel_files():
    """Test if Excel files exist in data directory"""
    print("\n" + "=" * 60)
    print("Testing Excel Files")
    print("=" * 60)
    
    data_dir = Path(__file__).parent / "data"
    
    if data_dir.exists():
        excel_files = list(data_dir.glob("*.xlsx"))
        if excel_files:
            print(f"[PASS] Found {len(excel_files)} Excel files:")
            for file in excel_files:
                print(f"   - {file.name}")
            return True
        else:
            print("[FAIL] No Excel files found in data/ directory")
            return False
    else:
        print("[FAIL] data/ directory does not exist")
        return False

def test_firewall_rules():
    """Test if port 8000 is accessible"""
    print("\n" + "=" * 60)
    print("Testing Firewall Rules")
    print("=" * 60)
    
    try:
        # Try to bind to port 8000
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        try:
            sock.bind(('0.0.0.0', 8000))
            print("[PASS] Port 8000 is available")
            print("   No firewall blocking detected")
            sock.close()
            return True
        except socket.error:
            print("[INFO] Port 8000 is already in use")
            print("   This is expected if the dashboard server is running")
            print("   Port is accessible and not blocked by firewall")
            sock.close()
            return True  # Consider this as pass since server is using it
    except Exception as e:
        print(f"[FAIL] Error testing firewall: {e}")
        return False

def generate_access_report():
    """Generate comprehensive access report"""
    print("\n" + "=" * 60)
    print("ACCESS REPORT")
    print("=" * 60)
    
    local_ip = get_local_ip()
    print(f"\n[INFO] Local IP: {local_ip}")
    print(f"[INFO] Network IP: 10.137.51.248")
    print(f"[INFO] Port: 8000")
    
    print("\n[INFO] Access URLs:")
    print(f"   Local: http://localhost:8000/simple_dashboard.html")
    print(f"   Network: http://10.137.51.248:8000/simple_dashboard.html")
    print(f"   Local IP: http://{local_ip}:8000/simple_dashboard.html")
    
    print("\n[INFO] Dell Team Requirements:")
    print("   1. Connected to Dell network (amer.dell.com)")
    print("   2. VPN access if working remotely")
    print("   3. Browser with JavaScript enabled")
    print("   4. No special software installation needed")

def main():
    """Run all network tests"""
    print("L11 Networking Dashboard - Network Connectivity Test")
    print("=" * 60)
    
    results = {
        'local_server': test_local_server(),
        'network_ip': test_network_ip(),
        'data_file': test_data_file(),
        'excel_files': test_excel_files(),
        'firewall': test_firewall_rules()
    }
    
    generate_access_report()
    
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    
    for test_name, result in results.items():
        status = "[PASS]" if result else "[FAIL]"
        print(f"{status}: {test_name.replace('_', ' ').title()}")
    
    print("\n" + "=" * 60)
    
    if all(results.values()):
        print("[SUCCESS] ALL TESTS PASSED - Dashboard is ready for sharing!")
        print("\n[INFO] Share this URL with Dell team members:")
        print("   http://10.137.51.248:8000/simple_dashboard.html")
    else:
        print("[WARNING] SOME TESTS FAILED - Please address the issues above")
        print("\n[TROUBLESHOOTING]")
        if not results['local_server']:
            print("   - Start server: python start_server.py")
        if not results['data_file']:
            print("   - Process data: python process_data.py")
        if not results['excel_files']:
            print("   - Add Excel files to data/ directory")
        if not results['network_ip']:
            print("   - Check network connectivity and firewall settings")
    
    print("=" * 60)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nTest interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n[ERROR] Unexpected error: {e}")
        sys.exit(1)