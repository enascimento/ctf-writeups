#!/usr/bin/env python3
import binascii
key = "yYpWfDuw"
def mystery(s):
    r = ""
    for i, c in enumerate(s):
        r += chr(ord(c) ^ ((i * ord(key[i % len(key)])) % 256))
    return binascii.hexlify(bytes(r, "utf-8"))

cipher = b"6538c2937cc3bb20c3983ac2ab4901c38fc297161fc2a6c3b3c281c28107c2a7c2a03fc3956ec3b55350"
def unmystery(s):
    r = ""
    for i, c in enumerate(s):
        r += chr(ord(c) ^ ((i * ord(key[i % len(key)])) % 256))
    return r

print(unmystery(binascii.unhexlify(cipher).decode("utf-8")))
