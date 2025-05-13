from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl
import socket

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
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        print("Encrypted POST data received")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Secure login received. (Check Wireshark - should be encrypted!)")

hostname = socket.gethostname()
port = 4443
httpd = HTTPServer(('0.0.0.0', port), SecureHandler)
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain(certfile="D:/networks/http/cert.pem", keyfile="D:/networks/http/cert.key")
httpd.socket = ssl_context.wrap_socket(httpd.socket, server_side=True)

print(f"Server started - visit: https://{hostname}:{port}")
print(f"Or try: https://localhost:{port}")
httpd.serve_forever()
