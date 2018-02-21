#! /usr/bin/env python3
##
# Created for EasyCTF 2018_Teaching Old Tricks New Dogs
# By Amos (LFlare) Ng <amosng1@gmail.com>
##N = int(input())
ciphertext = input()

plaintext = ""
for c in ciphertext:
    if c == " ":
        plaintext += c
        continue
    plaintext += chr(((ord(c)-ord('a')) - N) % 26 + ord('a'))

print(plaintext)
