#! /usr/bin/env python3
##
# Created for AngstromCTF 2018_Xor
# By Amos (LFlare) Ng <amosng1@gmail.com>
##
# Imports
import binascii

ciphertext = binascii.unhexlify("fbf9eefce1f2f5eaffc5e3f5efc5efe9fffec5fbc5e9f9e8f3eaeee7")
for key in range(255):
    plaintext = ""
    for c in ciphertext:
        plaintext += chr(c ^ key)
    if "ctf" in plaintext:
        print(plaintext)
