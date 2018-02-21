#! /usr/bin/env python3
##
# Created for the Visual Words challenge
# By Amos Ng
##
# Imports
import binascii
from PIL import Image

# Loaded image
img = Image.open('test.png').convert('RGB')
pix = img.load()

# Get image size
width, height = img.size

# Iter up to 50 characters just to test
flag = []
for i in range(0, 50):
    r, g, b = pix[i, 0]
    r = r >> 1
    g = g >> 1
    b = b >> 1

    flag.append(chr(r))
    flag.append(chr(g))
    flag.append(chr(b))

print("".join(flag))