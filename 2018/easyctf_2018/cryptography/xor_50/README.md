# EasyCTF_2018: xor

**Category:** Cryptography
**Points:** 50
**Description:**

>A flag has been encrypted using single-byte xor. Can you decrypt it? [File](https://easyctf.com/chals/autogen/90/xor.txt).

## Write-up
As a single-byte xor, this challenge is much more easily solved with a simple Python script.

    for i in range(255):
        plaintext = ""
        for c in data:
            plaintext += chr(c ^ i)

        if "easyctf" in plaintext:
            print(plaintext)

Full script available [here](solve.py).

    root@ctf:~/downloads# ./solve.py 
    easyctf{nsbtbzlfudpixosinwqfckqrx}

Therefore, the flag is `easyctf{nsbtbzlfudpixosinwqfckqrx}`.
