#! /usr/bin/env python3
##
# Created for CSAW CTF 2017
# By Amos (LFlare) Ng
##
# Imports
from pwn import *
import string

# Create tube
t = remote("crypto.chal.csaw.io", 1578)

# Loop
flag = ""
cookie = ""
# context.log_level = "debug"
with log.progress("Cracking flag...") as p:
    while True:
        for c in string.printable:
            # Receive placeholder
            t.recvuntil(": ")

            # Get initial flag
            p.status(flag + c)
            t.sendline(("\x00" * (31 - len(flag))) + flag + c + ("\x00" * (31 - len(flag))))
            t.recvuntil("is: ")
            cookie = t.recvline().decode()

            # Compare cookie
            if cookie[:64] == cookie[64:128]:
                flag += c
                break

        # If flag reached max length, break
        if len(flag) == 32:
            break

log.success(flag)
