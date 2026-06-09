import gnupg

gpg = gnupg.GPG()

fingerprint = "132C50BB35ED52D0F49069C8B533CFB4FDDA8B95"

with open("secret.txt", "rb") as f:
    status = gpg.encrypt_file(
        f,
        recipients=[fingerprint],
        output="secret.txt.gpg"
    )

print("Success:", status.ok)
print("Status :", status.status)