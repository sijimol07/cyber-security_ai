import jwt

with open("private_key.pem", "rb") as f:
    private_key = f.read()

with open("public_key.pem", "rb") as f:
    public_key = f.read()

token = jwt.encode(
    {"username": "alice"},
    private_key,
    algorithm="RS256"
)

print("TOKEN:")
print(token)

decoded = jwt.decode(
    token,
    public_key,
    algorithms=["RS256"]
)

print(decoded)