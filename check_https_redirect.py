import requests

url = "http://google.com"

response = requests.get(url, allow_redirects=True)

with open("https_redirect_report.txt", "w") as f:
    f.write(f"Final URL: {response.url}\n")
    f.write(f"Status Code: {response.status_code}\n")

    if response.url.startswith("https://"):
        f.write("HTTPS redirect enabled\n")
    else:
        f.write("HTTPS redirect NOT enabled\n")

print("Report saved to https_redirect_report.txt")