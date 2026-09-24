import http.server
import socketserver
import webbrowser
import os
from pathlib import Path

# Change to the script directory
script_dir = Path(__file__).parent.resolve()
os.chdir(script_dir)

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Server running at http://localhost:{PORT}")
    print(f"Open http://localhost:{PORT}/index.html in your browser")
    print("Press Ctrl+C to stop the server")
    
    # Automatically open the browser
    webbrowser.open(f'http://localhost:{PORT}/index.html')
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
