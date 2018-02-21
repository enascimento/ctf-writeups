# EasyCTF_2018: License Check

**Category:** Reverse Engineering
**Points:** 300
**Description:**

>I want a valid license for a piece of software, here is the license validation software. Can you give me a valid license for the email `mzisthebest@notarealemail.com`?
Note: flag is not in easyctf{} format.

## Write-up
Through lots of debugging, patching and pulling my hair out in ways that I actually do not know how to do a writeup on, I finally figured out how to bypass the debugger check by patching the binary too many times to count. Through masochistic analysis with ollydbg and too many cups of coffees, we can conclude 6 properties of the licenses for mzisthebest@notarealemail.com`.

1. The email `mzisthebest@notarealemail.com` generates a checksum of `1ae33`
2. The checksum is in base-30
3. License key is 16 characters in base-30
4. License key is split into 4 equal parts of 4 characters of base-30 each
5. Every part is then converted to its representive integers
6. Every part is then XORed together and the result **must** match the checksum

This can be then converted into a [Python](solve.py) representation and be used to generate our license key.

    $ ./solve.py 
    4ld70r4e43h043h0

Therefore, the flag is `4ld70r4e43h043h0`.
