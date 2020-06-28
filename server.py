#!/usr/bin/env python
import os
from http.server import HTTPServer, BaseHTTPRequestHandler

PORT = int(os.environ['PORT']) if "PORT" in os.environ else 3000

class S(BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-Type', 'plain/text')
    self.end_headers()
    self.wfile.write(b'Hello World')

with HTTPServer(('0.0.0.0', PORT), S) as httpd:
  print('Serving on localhost:{}'.format(PORT))
  httpd.serve_forever()
