import gnupg

gpg = gnupg.GPG()

print("Generating key...")

input_data = gpg.gen_key_input(
    name_real="Test User",
    name_email="test@example.com",
    passphrase="mypassword123"
)

key = gpg.gen_key(input_data)

print("Fingerprint:", key.fingerprint)

print("\nAvailable keys:")
for k in gpg.list_keys():
    print(k["fingerprint"])