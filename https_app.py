from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask HTTPS is running securely!"

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=4433,
        ssl_context=("server.crt", "server.key")
    )