import gnupg
#https://pythonhosted.org/python-gnupg/

#gpg = gnupg.GPG(gpgbinary="C:\\Program Files (x86)\\GnuPG\\bin\\gpg.exe", use_agent=True)
#gpg = gnupg.GPG(gnupghome="/tmp", use_agent=False) #doesnt ask for keycard password
gpg = gnupg.GPG() #dont store pin

#import key
#publicKey = open("key.pub", "r").read()
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
    if msg_decrypted.stderr:
        print(msg_decrypted.stderr)
    else:
        print(msg_decrypted)
    
    print(msg_decrypted)
