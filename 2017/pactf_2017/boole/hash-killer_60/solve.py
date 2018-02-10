#! /usr/bin/env python3
##
# Created for the Hash Killer challenge
# By Amos Ng
##
# Imports
import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES

# Setup ciphertext
cipher_b64 = "mJRKaaMSR1atUGs0kOkAJP3dty9tjCvXKMzWDHtZdRQ="
ciphertext = base64.b64decode(cipher_b64)

# Setup decryption parameters
key = "AES"
key = hashlib.md5(key.encode()).hexdigest()
obj = AES.new(key, AES.MODE_ECB)

# Decrypt
ciphertext = obj.decrypt(ciphertext)

# Print
print(ciphertext.decode())