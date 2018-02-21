#! /usr/bin/env python3
##
# Created for the GovTech Binary Challenge Level 2
# By Amos <LFlare> Ng
##
# Import libraries
import hashlib

# Satisfy input string
flag = "flag1{7171a60f8cf4a789b7fa5906aa78f3e7}"

# Loop
for i in range(1000000):
    flag = hashlib.md5((flag + str(i)).encode()).hexdigest()
    if flag.startswith("00000"):
        print("flag2{%s}" % flag)
        break
