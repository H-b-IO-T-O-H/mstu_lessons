#!/usr/bin/env python3
"""
Very simple HTTP server in python for logging requests
Usage::
    ./http_server.py [<port>]
"""
from http.server import BaseHTTPRequestHandler, HTTPServer, CGIHTTPRequestHandler

PORT_NUMBER = 8080


class MyHandler(BaseHTTPRequestHandler):
    # Handler for the GET requests
    def do_GET(self):
        print('Get request received')
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # Send the html message
        self.wfile.write(b"Hello World !")
        return


class Server:
    def __init__(self):
        # Create a web server and define the handler to manage the
        # incoming request
        # self.server = HTTPServer(('', PORT_NUMBER), CGIHTTPRequestHandler)
        self.server = HTTPServer(('', PORT_NUMBER), MyHandler)

    def run(self, port):
        try:
            print('Started httpserver on port ', port)
            # Wait forever for incoming http requests
            self.server.serve_forever()

        except KeyboardInterrupt:
            print('Shutting down the web server')
            self.server.socket.close()


if __name__ == '__main__':
    from sys import argv

    server = Server()
    if len(argv) == 2:
        server.run(port=int(argv[1]))
    else:
        server.run(port=PORT_NUMBER)
