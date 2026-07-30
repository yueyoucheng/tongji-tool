import io, os
from http.server import HTTPServer, SimpleHTTPRequestHandler
import cgi, json

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = "/index.html"
        return super().do_GET()

    def do_POST(self):
        if self.path == "/process":
            form = cgi.FieldStorage(fp=self.rfile, headers=self.headers, environ={"REQUEST_METHOD": "POST"})
            files = form.getlist("data_files")
            tpl = form["template_file"]
            # Process using openpyxl
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_error(404)

HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
