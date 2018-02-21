#! /usr/bin/env python3
##
# Created for EasyCTF 2018_License Check
# By Amos (LFlare) Ng <amosng1@gmail.com>
##
# Imports
import string
import random

# Functions
## https://stackoverflow.com/a/2267446
def int2base(x, base):
    cs = string.digits + string.ascii_letters
    if x < 0:
        sign = -1
    elif x == 0:
        return cs[0]
    else:
        sign = 1

    x *= sign
    digits = []

    while x:
        digits.append(cs[x % base])
        x //= base

    if sign < 0:
        digits.append('-')

    digits.reverse()

    return ''.join(digits)

# Derived from ollydbg
checksum = 0x1ae33

# Get balancing xor
balance = random.randrange(checksum)

# Get xored first quarter
xored = balance ^ checksum

# Prepare license
license = int2base(xored, 30).zfill(4)
license += int2base(balance, 30).zfill(4)

# Fill in ending
random_ending = random.randrange(30**4)
license += int2base(random_ending, 30).zfill(4) + int2base(random_ending, 30).zfill(4)

# Print our new "generated" license!
print(license)
