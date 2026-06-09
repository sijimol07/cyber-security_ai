import requests

url = "https://example.com"

response = requests.get(url, timeout=10)

security_headers = [
    "Content-Security-Policy",
    "Strict-Transport-Security",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy"
]

for header in security_headers:
    value = response.headers.get(header)
    print(f"{header}: {value if value else 'MISSING'}")