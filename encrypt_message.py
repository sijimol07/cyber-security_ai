import gnupg
import tempfile

# Initialize GPG
gpg = gnupg.GPG()

# Example public key file
with open("recipient_public_key.asc", "r") as f:
    key_data = f.read()

# Import recipient's public key
import_result = gpg.import_keys(key_data)

if not import_result.fingerprints:
    raise Exception("Failed to import public key")

fingerprint = import_result.fingerprints[0]
print("Imported key:", fingerprint)

# Encrypt a message
message = "Hello, this is a secret message."

encrypted_data = gpg.encrypt(
    message,
    recipients=[fingerprint]
)

if not encrypted_data.ok:
    raise Exception(f"Encryption failed: {encrypted_data.status}")

print("Encrypted message:")
print(str(encrypted_data))

# Save encrypted message
with open("message.gpg", "w") as f:
    f.write(str(encrypted_data))