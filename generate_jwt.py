import jwt
from datetime import datetime, timedelta, timezone

with open("private_key.pem", "rb") as f:
    private_key = f.read()

payload = {
    "sub": "alice",
    "iat": datetime.now(timezone.utc),
    "exp": datetime.now(timezone.utc) + timedelta(hours=1)
}

token = jwt.encode(
    payload,
    private_key,
    algorithm="RS256"
)

print(token)