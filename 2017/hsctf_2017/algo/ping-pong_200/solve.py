#! /usr/bin/env python3
##
# Created for the Ping Pong challenge
# By Amos Ng
##
from pwn import *


t = remote("104.131.90.29", 8007)
t.recvuntil("Enter an empty line when you are done ==>\n")

with open("solution", "r") as file:
    data = file.read()
    t.send(data)

# Last empty line
t.sendline()

# Get flag
flag = t.recvline().decode()
log.success(flag)