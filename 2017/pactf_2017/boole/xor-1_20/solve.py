#! /usr/bin/env python3
##
# Created for the XOR 1 challenge
# By Amos Ng
##
ciphertext = "KGZFK\qZFG]qA\qZFOZ"

for i in range(255):
    plaintext = ""
    for c in ciphertext:
        pc = i ^ ord(c)
        plaintext += chr(pc)
    print(plaintext)