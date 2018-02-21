#! /usr/bin/env python3
##
# Created for EasyCTF 2018_
# By Amos (LFlare) Ng <amosng1@gmail.com>
##
from zipfile import ZipFile
import os
import string
import hashlib

filename = "begin.zip"
password = b"coolkarni"
hashed = ""

# Simple stepping function wrapper
def step(pattern, cs, index=0):
    pattern = list(pattern)
    pattern[index] = cs[0]
    return "".join(pattern)

# Function to push patterns
def generate_next(pattern, index=0):
    c = pattern[index]

    if c != "_":
        # Detect bruteforce means
        if c.isdigit():
            cs = string.digits
        elif c.islower():
            cs = string.ascii_lowercase
        elif c.isupper():
            cs = string.ascii_uppercase

        # Get index and size of charset
        next_i = cs.index(c) + 1
        max_i = len(cs)

        # If we reached end of charset, loopback
        if (next_i == max_i):
            pattern = step(pattern, cs[0], index)
            pattern = generate_next(pattern, index+1)
        else:
            pattern = step(pattern, cs[next_i], index)
    else:
        pattern = generate_next(pattern, index+1)

    return pattern

# Generate next patterns
def generator(pattern):
    while True:
        yield pattern
        pattern = generate_next(pattern)
        if pattern is None:
            break

# Check if we are already cracking halfway
if not os.path.isfile("filename.txt"):
    with ZipFile(filename) as zip:
        zip.extractall(pwd=password)

# While flag not found
while not os.path.isfile("flag.txt"):
    with open("pattern.txt") as file:
        pattern = file.read().strip()
    with open("filename.txt") as file:
        filename = file.read().split("/")[1].strip()
    with open("hash.txt") as file:
        hashed = file.read().strip()

    print(f"ATTEMPTING: {pattern}")
    for attempt in generator(pattern):
        if hashed == hashlib.sha1(attempt.encode()).hexdigest():
            print(f"SUCCESS: {attempt}")
            with ZipFile(filename) as zip:
                zip.extractall(pwd=attempt.encode())
                break

# Try to read flag
with open("flag.txt") as file:
    flag = file.read().strip()
    print(flag)
