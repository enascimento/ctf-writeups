#! /usr/bin/env python3
##
# Created for the Go Deep challenge
# By Amos Ng
##
import base64
import binascii


# Import file
with open("godeep.txt", "r") as file:
    data = file.read()

# Conversion rabbit hole
data = binascii.unhexlify(data[:-1])
data = base64.b64decode(data)
data = base64.b64decode(data)
data = base64.b64decode(data)
data = base64.b64decode(data)
data = base64.b64decode(data)
data = binascii.unhexlify(data)
data = base64.b64decode(data)
data = base64.b64decode(data)
data = binascii.unhexlify(data)
data = base64.b64decode(data)
data = base64.b64decode(data)
data = base64.b64decode(data)
data = binascii.unhexlify(data)
data = base64.b64decode(data)
data = base64.b64decode(data)
data = base64.b64decode(data)
data = base64.b64decode(data)
data = binascii.unhexlify(data)
data = base64.b64decode(data)
data = binascii.unhexlify(data)
data = base64.b64decode(data)
data = binascii.unhexlify(data)
data = binascii.unhexlify(data)
print(data.decode())