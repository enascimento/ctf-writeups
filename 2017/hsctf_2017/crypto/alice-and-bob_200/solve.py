#! /usr/bin/env python3
##
# Created for the Alice and Bob challenge
# By Amos Ng
##
import math
import sys


# Values we are given
g = 987
p = 8911991767204557841
A = 731665363559374475
B = 1317032838957486192

# Better function
def brute(g, A, p):
    for a in range(sys.maxsize):
        if pow(g, a, p) == A:
            return a


a = brute(g, A, p)
b = brute(g, B, p)
assert a == 1213832
assert b == 1201905
print("a: %d, b: %d" % (a, b))

# Calculate shared secret
K = pow(A, b, p)
assert K == 1715359156632385906

print("K: %d" % K)