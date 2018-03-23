#! /usr/bin/env python3
##
import gmpy2
import struct
import binascii

def lcg(m, a, c, x):
    return (a*x + c) % m

m = pow(2, 32)
data = open("flag.png.enc", "rb").read()

x1 = int.from_bytes(data[:4], "big") ^ int.from_bytes(b"\x89\x50\x4e\x47", "big")
x2 = int.from_bytes(data[4:8], "big") ^ int.from_bytes(b"\x0d\x0a\x1a\x0a", "big")
x3 = int.from_bytes(data[8:12], "big") ^ int.from_bytes(b"\x00\x00\x00\x0d", "big")
print("x1: ", x1)
print("x2: ", x2)
print("x3: ", x3)

def get_a(m, seq):
    k = (seq[0] - seq[1]) % m
    inv = int(gmpy2.invert(k, m))
    return (inv * (seq[1] - seq[2])) % m

a = get_a(m, [x1, x2, x3])
print("a: ", a)

c = (x2 - (x1 * a)) % m
print("c: ", c)

print("=== VERIFY ===")
print("x1: ", x1)
print("x2: ", lcg(m, a, c, x1))
print("x3: ", lcg(m, a, c, lcg(m, a, c, x1)))

data = [data[i:i+4] for i in range(0, len(data), 4)]
x = x1
e = bytes()
for i in range(len(data)):
    e += struct.pack('>I', x ^ struct.unpack('>I', data[i])[0])
    x = lcg(m, a, c, x)

with open('flag.png', 'wb') as f:
    f.write(e)
    f.close()
