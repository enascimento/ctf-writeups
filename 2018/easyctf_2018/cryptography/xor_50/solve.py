#! /usr/bin/env python3
##
# Created for EasyCTF 2018_Xor
# By Amos (LFlare) Ng <amosng1@gmail.com>
##
with open("xor.txt", "rb") as file:
    data = file.read()

    for i in range(255):
        plaintext = ""
        for c in data:
            plaintext += chr(c ^ i)

        if "easyctf" in plaintext:
            print(plaintext)
