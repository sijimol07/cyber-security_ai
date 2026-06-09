import requests
import json

url = "https://example.com"

report = {}

try:
    response = requests.get(url, timeout=10)

    report["status_code"] = response.status_code
    report["server"] = response.headers.get("Server", "Hidden")

    headers_to_check = [
        "Content-Security-Policy",
        "Strict-Transport-Security",
        "X-Frame-Options",
        "X-Content-Type-Options"
    ]

    report["security_headers"] = {}

    for header in headers_to_check:
        report["security_headers"][header] = (
            response.headers.get(header, "Missing")
        )

except Exception as e:
    report["error"] = str(e)

with open("website_security_audit.json", "w") as f:
    json.dump(report, f, indent=4)

print("Audit saved to website_security_audit.json")