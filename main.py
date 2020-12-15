from http.server import HTTPServer, BaseHTTPRequestHandler


class IIDServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = "/index.html"

        try:
            page_data = open("pages" + self.path).read()
            self.send_response(200)
        except Exception as e:
            page_data = open("pages/not_found.html").read()
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(page_data, 'utf-8'))


http_daemon = HTTPServer(('localhost', 80), IIDServer)
http_daemon.serve_forever()
