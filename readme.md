# GPG Demo Project for Windows and Linux

Linux Version: [linux.md](./linux.md)

Windows Version: [win.md](./win.md)

## Setup Card (Linux only Version)

```bash
sudo apt-get install libccid scdaemon gpg python3-usb
```

work with card:

```bash
gpg --card-status | grep Version
gpg --card-edit
```

❗ Remember: Setting User and Reset Pin only works **after** installing a Key

```c
Admin PIN default: 12345678
User PIN default : 123456
```

Create new Key
https://www.nitrokey.com/de/documentation/openpgp-create-backup

```bash
gpg/card> generate
```

## Bash-PoC

```bash
echo "das ist geheim" | gpg --encrypt --armor --recipient test@web.de > file.enc
gpg --decrypt < file.enc

## (optional add pin)
# gpg --passphrase 654321 --decrypt < file.enc
```