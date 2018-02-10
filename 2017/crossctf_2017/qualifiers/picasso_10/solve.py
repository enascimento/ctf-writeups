#! /usr/bin/env python3
##
# Created for the Picasso challenge
# By Amos Ng
##
from PIL import Image


# Load image
img = Image.open('flag.png').convert('RGB')
pix = img.load()

# Get image size
width, _ = img.size

# Count pixels before pixel change
flag = []
count = 0
for i in range(width):
    r, g, b = pix[i, 0]

    if r == 0 or g == 0 or b == 0:
        flag.append(chr(count))
        count = 0
    else:
        count += 1

print("".join(flag))