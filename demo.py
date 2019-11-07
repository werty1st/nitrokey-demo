import sys
import gpg

with gpg.Context(armor=True) as c:
    recipients = []
    print("Enter name of your recipient(s), end with a blank line.")
    #while True:
    line = "adams.r@zdf.de" #input()
    # if not line:
    #     break
    new = list(c.keylist(line))
    if not new:
        print("Matched no known keys.")
    else:
        print("Adding {}.".format(", ".join(k.uids[0].name for k in new)))
        recipients.extend(new)

    if not recipients:
        sys.exit("No recipients.")

    print("Encrypting for {}.".format(", ".join(
        k.uids[0].name for k in recipients)))

    ciphertext, _, _ = c.encrypt(b"This is my message,", recipients)
    sys.stdout.buffer.write(ciphertext)