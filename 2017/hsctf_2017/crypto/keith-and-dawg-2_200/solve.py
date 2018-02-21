#! /usr/bin/env python3
##
# Created for the Remember MD5 challenge
# By Amos Ng
##
import hashlib
import pickle
import sys
from itertools import product

def permutation_atindex(_int, _set, length):
    items = []
    strLength = len(_set)
    index = _int % strLength
    items.append(_set[index])

    for n in range(1,length, 1):
        _int //= strLength
        index = _int % strLength
        items.append(_set[index])

    return items

class PermutationIterator:
    def __init__(self, iterable, length):
        self.length = length
        self.current = 0
        self.max = len(iterable) ** length
        self.iterable = iterable
    def __iter__(self):
        return self
    def __next__(self):
        if self.current >= self.max:
            raise StopIteration
        try:
            return permutation_atindex(self.current, self.iterable, self.length)
        finally:
            self.current   += 1

for r in range(16):
    counter = 0
    for perm in PermutationIterator("qwerty", r):
        counter += 1
        perm = "".join(perm)
        if (counter % 100000 == 0):
            print(perm)
        hash = hashlib.md5(perm.encode()).hexdigest()
        if "b81b28baa97b04cf3508394d9a58caae" in hash:
            assert perm == "ywterqtwe"
            print("Flag %s" % (perm))
            sys.exit(0)