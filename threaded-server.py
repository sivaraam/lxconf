#!/usr/bin/env python3
#
# A simple Python3 program that starts a HTTP server
# in threaded mode to allow parallel requests.
#
# It accepts two aguments.
#
#  1. Port in which to start the server
#  2. Directory in which to start the server
#
# Both of them optional. If unspecified, the
# server starts in port 8176 serving contents
# of the current directory.
#

import http.server
import socketserver
import sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8176
DIRECTORY = str(sys.argv[2]) if len(sys.argv) > 2 else "."

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

class ThreadedHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True

server = ThreadedHTTPServer(('', PORT), Handler)

try:
    print("serving at port", PORT)
    server.serve_forever()
except KeyboardInterrupt:
    pass

