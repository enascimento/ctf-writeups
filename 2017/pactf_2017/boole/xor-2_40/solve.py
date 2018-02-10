#! /usr/bin/env python3
##
# Created for XOR 2 challenge
# By Amos Ng
##
# Import file
with open("Article.txt", "r") as file:
    cipherhex = file.read()
    cipherbytes = bytes.fromhex(cipherhex[:-1])