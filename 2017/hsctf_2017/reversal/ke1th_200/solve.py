#! /usr/bin/env python3
##
# Created for the KE1TH challenge
# By Amos Ng
##
from base64 import *
from Crypto.Cipher import AES


# Calculate IV bytes
iv = [10, -73, -33, -65, 87, 87, -121, -41, -16, 89, 12, 31, 7, 82, -43, -100]
for k, i in enumerate(iv):
    iv[k] = int(i) & 0xff
iv = bytes(iv)

# Calculate correct string bytes
ciphertext_string = "-93^35^23^82^-4^57^-128^83^-95^-60^-100^73^40^-86^7^73^-101^3^118^-66^-104^69^121^76^1^-124^-124^-1^-64^29^28^43^2^-25^54^52^-79^-62^11^-43^52^-72^-117^-25^-103^-55^75^-97^"
ciphertext_list = []
for c in ciphertext_string.split("^")[:-1]:
    c = int(c) & 0xff
    ciphertext_list.append(c)
ciphertext = bytes(ciphertext_list)

# Calculate AES key
key_b64 = "/Vl4PKzS9d+Vm/0eePmaYw=="
key = b64decode(key_b64)

def unpad(b):
    return b[:-b[-1]]

cipher = AES.new(key, AES.MODE_CBC, iv)
plaintext = unpad(cipher.decrypt(ciphertext)).decode()

print("Flag: %s" % plaintext)