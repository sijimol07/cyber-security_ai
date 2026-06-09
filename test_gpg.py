import gnupg

gpg = gnupg.GPG()

print("Version:", gpg.version)
print("Home:", gpg.gnupghome)