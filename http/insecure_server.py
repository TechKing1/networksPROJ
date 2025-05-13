from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"""
                <html><body>
                <h2>Login Form (Insecure)</h2>
                <form method="POST" action="/login">
                    Username: <input type="text" name="username"><br>
                    Password: <input type="password" name="password"><br>
                    <input type="submit" value="Login">
                </form>
                </body></html>
            """)
        else:
            self.send_error(404)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        print("Captured POST data:", post_data.decode())

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Login received (insecurely). Check your terminal and Wireshark.")

httpd = HTTPServer(('localhost', 8080), SimpleHTTPRequestHandler)
print("Serving on http://localhost:8080 ...")
httpd.serve_forever()