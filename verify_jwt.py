import jwt

with open("public_key.pem", "rb") as f:
    public_key = f.read()

token = input("Paste JWT: ")

try:
    payload = jwt.decode(
        token,
        public_key,
        algorithms=["RS256"]
    )

    print("Valid token")
    print(payload)

except jwt.ExpiredSignatureError:
    print("Token expired")

except jwt.InvalidTokenError as e:
    print("Invalid token:", e)