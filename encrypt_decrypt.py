import gnupg

gpg = gnupg.GPG()

fingerprint = "132C50BB35ED52D0F49069C8B533CFB4FDDA8B95"

message = "Hello from Python GPG!"

# Encrypt
encrypted = gpg.encrypt(
    message,
    recipients=[fingerprint]
)

if not encrypted.ok:
    print("Encryption failed:", encrypted.status)
    exit()

print("=== ENCRYPTED ===")
print(str(encrypted))

# Decrypt
decrypted = gpg.decrypt(
    str(encrypted),
    passphrase="mypassword123"  # use the passphrase from key generation
)

if not decrypted.ok:
    print("Decryption failed:", decrypted.status)
    exit()

print("\n=== DECRYPTED ===")
print(decrypted.data.decode())