#! /usr/bin/env python3
##
# Created for the Trivial.pyc challenge
# By Amos Ng
##
check_code = "AK4782"
numbers = 18529313.0 / 2.0
change = "standardisation"[::2]
template = "CrossCTF{%s_%d_%s}"

flag = template % (change, numbers, check_code)
print(flag)