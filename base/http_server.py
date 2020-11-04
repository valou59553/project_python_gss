import http.server, os, webbrowser, socketserver
from flask import Flask

port = 8000
address = ("", port)

handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(address, handler)

print("serveur démarré sur PORT %s"%(port))

httpd.serve_forever()