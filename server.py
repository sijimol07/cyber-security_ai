import http.server
import ssl

server_address = ("localhost", 4443)

httpd = http.server.HTTPServer(
    server_address,
    http.server.SimpleHTTPRequestHandler
)

# Create SSL context (modern way)
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)

context.load_cert_chain(
    certfile="server.crt",
    keyfile="server.key"
)

# Wrap socket using context
httpd.socket = context.wrap_socket(
    httpd.socket,
    server_side=True
)

print("Running HTTPS server at https://localhost:4443")
httpd.serve_forever()