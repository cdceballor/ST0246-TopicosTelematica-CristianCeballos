from http.server import BaseHTTPRequestHandler
from urllib import parse
import echo_server

class GetHandler(BaseHTTPRequestHandler):
    echo_server


if __name__ == '__main__':
    from http.server import HTTPServer
    server = HTTPServer(('localhost', 8080), GetHandler)
    print('Starting server, use <Ctrl-C> to stop')
    server.serve_forever()