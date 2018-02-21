#! /usr/bin/env python3
##
from binascii import unhexlify
from operator import attrgetter

def functionB(d): # fiips the integer
    soup = 0
    while d != 0:
        soup = (soup * 10) + (d % 10)
        d //= 10
    return soup

def functionA(digits): # glorified integer converter
    soup = 0
    for digit in digits:
        soup *= 10
        soup += ord(digit) - ord('0')
    return soup

def main():
    inputDigit = input()[:7]
    print(inputDigit)
    if not attrgetter('isdigit')(inputDigit)():
        print("that's not a number lol")
        return

    soup = functionB(functionA(inputDigit))
    hexed = attrgetter('zfill')(hex(soup)[2:])(8)[-8:]
    if unhexlify(hexed) == attrgetter('encode')('s0up')():
        with open('flag.txt', 'r') as file:
            print("oh yay it's a flag!", attrgetter('read')(file)())
    else:
        print('oh noes rip u')

if __name__ == '__main__':
    main()

