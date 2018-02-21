# EasyCTF_2018: Teaching Old Tricks New Dogs

**Category:** Programming
**Points:** 40
**Description:**

>You can decode a Caesar cipher, but can you write a program to decode a Caesar cipher?
Your program will be given 2 lines of input, and your program needs to output the original message.
First line contains N, an integer representing how much the key was shifted by. 1 <= N <= 26
Second line contains the ciphertext, a string consisting of lowercase letters and spaces.
For example:
`6`
`o rubk kgyeizl`
You should print
`i love easyctf`

## Write-up
[Dead simple challenge](solve.py),

    ciphertext = input()

    plaintext = ""
    for c in ciphertext:
        if c == " ":
            plaintext += c
            continue
        plaintext += chr(((ord(c)-ord('a')) - N) % 26 + ord('a'))

    print(plaintext)

Therefore, there is no flag.
