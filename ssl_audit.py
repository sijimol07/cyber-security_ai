import ssl
import socket
from datetime import datetime, timezone

def get_cert(host):
    context = ssl.create_default_context()

    with socket.create_connection((host, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=host) as ssock:
            return ssock.getpeercert()

def analyze_ssl(host):
    cert = get_cert(host)

    print("Subject:", cert.get("subject"))
    print("Issuer:", cert.get("issuer"))
    print("Valid From:", cert.get("notBefore"))
    print("Valid Until:", cert.get("notAfter"))

    expiry = datetime.strptime(cert["notAfter"], "%b %d %H:%M:%S %Y %Z")

    # FIX: timezone-aware datetime
    days_left = (expiry - datetime.now(timezone.utc)).days

    print("Days until expiry:", days_left)

# Run test
analyze_ssl("google.com")