#! /usr/bin/env python3
##
# Created for the Coin Flip challenge
# By Amos Ng
##
import collections


# Read file
with open("file.txt", "r") as file:
    data = file.read().strip()

# Setup counter
counter = collections.Counter()

# Loop through data and count
count = 1
previous = data[0]
for i, c in enumerate(data):
    # Count first, remove later
    count += 1
    counter[count] += 1

    if c != previous:
        count = 1
        previous = c
    else:
        counter[count] -= 1

# Prepare flag
flag = ", ".join([str(v) for k, v in sorted(counter.items())])
assert flag == "249368, 124813, 62558, 31388, 15476, 7891, 3975, 1982, 943, 486, 270, 107, 64, 33, 15, 8, 4, 1, 1, 1"

print("Flag: %s" % flag)