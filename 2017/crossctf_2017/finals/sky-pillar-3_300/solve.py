#! /usr/bin/env python3
##
# Created for the Sky Pillar 3 challenge
# By Amos <LFlare> Ng
##
# Glorified bit counter
def magic(num):
    modulo = 0
    while num:
        modulo += (num & 0x1)
        num //= 2
    return modulo

# Try generating printable flag
payload = []
for i in range(0x30, 0x7e):
    magik = magic(i)

    # If matches requirements
    if (len(payload) == 0 and magik == 2) or \
       (len(payload) == 1 and magik == 1) or \
       (len(payload) == 2 and magik == 3) or \
       (len(payload) == 3 and magik == 2) or \
       (len(payload) == 4 and magik == 4):
        payload.append(chr(i))

# Print flag
print("Flag: %s" % " ".join(payload))
