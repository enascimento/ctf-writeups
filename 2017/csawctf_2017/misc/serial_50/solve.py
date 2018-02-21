#! /usr/bin/env python3
##
# Created for CSAW CTF 2017
# By Amos (LFlare) Ng <amosng1@gmail.com>
##
# Imports
from pwn import *

# Create tube
t = remote("misc.chal.csaw.io", 4239)

# Receive initial canned text
t.recvuntil("retransmit.\n")

# Receive serial messages
while True:
    # Get first initial transmission
    response = t.recvline().decode()
    char = None

    # Check until parity is correct
    while True:
        t.sendline("0")
        response = t.recvline().decode()
        char = response[1:9]
        parity = response[9:10]

        # Check parity, if correct, break out
        if char.count("1") % 2 == int(parity):
            break

    # Print flag character
    char = chr(int(char, 2))
    print(char, end="")

    # Proceed to next message
    t.sendline("1")
