import ssl
import socket
from datetime import datetime

hostname = "example.com"

context = ssl.create_default_context()

with socket.create_connection((hostname, 443)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        cert = ssock.getpeercert()

expiry_date = datetime.strptime(
    cert["notAfter"],
    "%b %d %H:%M:%S %Y %Z"
)

with open("ssl_report.txt", "w") as f:
    f.write(f"Host: {hostname}\n")
    f.write(f"Certificate Expiry: {expiry_date}\n")

print("Report saved to ssl_report.txt")