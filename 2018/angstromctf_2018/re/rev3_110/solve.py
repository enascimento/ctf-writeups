#! /usr/bin/env python3
##
# Created for AngstromCTF 2018_Rev3
# By Amos (LFlare) Ng <amosng1@gmail.com>
##
# Read
data = open("encoded.txt").read()

# Decode
for c in data:
    c = (ord(c) + 0x3) ^ 0x9
    print(chr(c), end="")

# Print
print()
