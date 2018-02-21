#! /usr/bin/env python3
##
# Created for EasyCTF 2018_Special Endings
# By Amos (LFlare) Ng <amosng1@gmail.com>
##
from base64 import b64decode, b64encode
from binascii import hexlify, unhexlify
import string

table = string.ascii_uppercase + string.ascii_lowercase + string.digits + "+/"
flag = ""

# Ease function
def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

# Get base64 data
with open("encrypted.txt") as file:
    data = file.readlines()

for original in data:
    # Get normal base64
    normal = b64encode(b64decode(original)).decode()
    padcount = original.count("=")

    # Get differences
    diff = 0
    for a, b in zip(original, normal):
        if a != b:
            diff = abs(table.index(a) - table.index(b))
            break

    # If there is a difference
    if diff:
        binary = bin(diff)[2:].zfill(padcount * 2)
        flag += binary
    else:
        flag += '0' * padcount * 2
        
# Format final flag
flag = "".join(chr(int(part, 2)) for part in chunks(flag, 8))
print(f"easyctf{{{flag}}}")
