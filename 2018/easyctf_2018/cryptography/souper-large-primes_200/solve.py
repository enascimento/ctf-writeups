#! /usr/bin/env python3
##
# Created for EasyCTF 2018_Souper Large Primes
# By Amos (LFlare) Ng <amosng1@gmail.com>
##
import gmpy2
import binascii

# Importing
with open("n.txt") as file:
    n = int(file.read())
    
with open("e.txt") as file:
    e = int(file.read())

with open("c.txt") as file:
    c = int(file.read())

# Broken with Fermat factoring
with open("p.txt") as file:
    p = int(file.read(), 16)

with open("q.txt") as file:
    q = int(file.read(), 16)

# Use CRT to decrypt
dp = gmpy2.invert(e, (p-1))
dq = gmpy2.invert(e, (q-1))
qinv = gmpy2.invert(q, p)

# Get message
m1 = gmpy2.powmod(c, dp, p)
m2 = gmpy2.powmod(c, dq, q)
h = (qinv * (m1 - m2)) % p 
m = m2 + h * q

# Save progress in m.txt
with open("m.txt", "w") as file:
    file.write(str(m))

# Print m
print(m)
