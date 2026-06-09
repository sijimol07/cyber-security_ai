import gnupg

gpg = gnupg.GPG()

with open("secret.txt.gpg", "rb") as f:
    status = gpg.decrypt_file(
        f,
        passphrase="mypassword123",
        output="secret_decrypted.txt"
    )

print("Success:", status.ok)