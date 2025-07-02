#!/usr/bin/env python3
import http.server
import socketserver
import base64
import os
from urllib.parse import urlparse

# Import configuration
try:
    from auth_config import USERNAME, PASSWORD, PORT, USERS
except ImportError:
    # Fallback configuration if config file doesn't exist
    USERNAME = "mawney"
    PASSWORD = "partners2024"
    PORT = 8000
    USERS = {USERNAME: PASSWORD}

class AuthHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_AUTHHEAD(self):
        self.send_response(401)
        self.send_header('WWW-Authenticate', 'Basic realm="Mawney Partners Market Map"')
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        # Check if user is authenticated
        if not self.is_authenticated():
            self.do_AUTHHEAD()
            self.wfile.write(b'Authentication required')
            return

        # Serve the file normally if authenticated
        super().do_GET()

    def is_authenticated(self):
        auth_header = self.headers.get('Authorization')
        if not auth_header:
            return False
        
        try:
            # Parse the Authorization header
            auth_type, auth_string = auth_header.split(' ', 1)
            if auth_type.lower() != 'basic':
                return False
            
            # Decode the credentials
            decoded = base64.b64decode(auth_string).decode('utf-8')
            username, password = decoded.split(':', 1)
            
            # Check credentials against USERS dictionary
            return username in USERS and USERS[username] == password
        except:
            return False

if __name__ == "__main__":
    print(f"Starting password-protected server on port {PORT}")
    print(f"Available users: {', '.join(USERS.keys())}")
    print(f"Access your site at: http://localhost:{PORT}")
    print("Press Ctrl+C to stop the server")
    
    with socketserver.TCPServer(("", PORT), AuthHTTPRequestHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.") 