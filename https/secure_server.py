from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl
import socket
import os
import sys

# === CONFIG ===
CERT_FILE = "cert.pem"
KEY_FILE = "D:/networks/networksPROJ/.gitignore/cert.key"
PORT = 4443

# === Check if certificate and key exist ===
if not os.path.exists(CERT_FILE) or not os.path.exists(KEY_FILE):
    print(f"❌ ERROR: Certificate or key file not found.")
    print(f"Expected files: {CERT_FILE} and {KEY_FILE}")
    print("👉 Generate them with the following command:")
    print("   openssl req -new -x509 -keyout cert.key -out cert.pem -days 365 -nodes")
    sys.exit(1)

# === HTTPS Server ===
class SecureHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"""
            <html><body>
            <h2>Login Form (Secure)</h2>
            <form method="POST" action="/login">
                Username: <input type="text" name="username"><br>
                Password: <input type="password" name="password"><br>
                <input type="submit" value="Login">
            </form>
            </body></html>
        """)

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        print("\n🔐 Encrypted POST data received (you won't see contents here if using HTTPS)")
        print(f"Raw data: {post_data}")  # for debug – won't show plaintext if encrypted
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Secure login received. (Check Wireshark - should be encrypted!)")

# === Set up HTTPS Server ===
hostname = socket.gethostname()
httpd = HTTPServer(('0.0.0.0', PORT), SecureHandler)

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain(certfile=CERT_FILE, keyfile=KEY_FILE)
httpd.socket = ssl_context.wrap_socket(httpd.socket, server_side=True)

# === Start Server ===
print(f"\n🚀 Server started successfully!")
print(f"Visit: https://{hostname}:{PORT}")
print(f"Or try: https://localhost:{PORT}\n")
httpd.serve_forever()
