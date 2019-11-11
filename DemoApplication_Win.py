import gnupg
#https://pythonhosted.org/python-gnupg/

gpg = gnupg.GPG(gpgbinary="C:\\Program Files (x86)\\GnuPG\\bin\\gpg.exe", use_agent=True)

#import key
with open("key.pub", "r") as file:
    publicKey = file.read()
    file.close()
import_result = gpg.import_keys(publicKey)
public_keys = gpg.scan_keys("key.pub")
for key in public_keys:
    print(key["uids"],str(import_result.fingerprints))

#encrypt
secretString = open("secret.txt", "r").read()
encrypted_ascii_data = gpg.encrypt(secretString, import_result.fingerprints, always_trust=True)
print( encrypted_ascii_data )
with open("secret.txt.enc", "wb") as file:
    file.write( encrypted_ascii_data.data )
    file.close()


#decrypt
with open("secret.txt.enc", "rb") as file:
    msg_enc = file.read()
    file.close()
    msg_decrypted = gpg.decrypt(msg_enc, always_trust=True)
    if not msg_decrypted.ok:
        print(msg_decrypted.stderr)
    else:
        print(msg_decrypted.status)    
        print()
        print(msg_decrypted)
