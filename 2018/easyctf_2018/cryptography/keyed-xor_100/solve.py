#! /usr/bin/env python3
##
# Created for EasyCTF 2018_Keyed Xor
# By Amos (LFlare) Ng <amosng1@gmail.com>
##
# Imports
from itertools import cycle

# Read encrypted flag
with open("keyed_xor", "rb") as file:
    data = file.read()

# key = "easyctf{"
key = "drivelling"

# Import wordlist
with open("wordlist.txt", "r") as file:
    wordlist = file.read().split("\n")

# Check for word in wordlist
for word in wordlist:
    current_key = key + word
    attempt = ""
    for a, b in zip(cycle(key + word), data):
        attempt += chr(ord(a) ^ b)

    if "flagflagflag" in attempt:
        print(word, attempt)
