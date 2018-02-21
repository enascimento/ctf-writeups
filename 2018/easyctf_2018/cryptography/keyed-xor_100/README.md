# EasyCTF_2018: Keyed Xor

**Category:** Cryptography
**Points:** 100
**Description:**

>A flag has been encrypted using keyed xor. Can you decrypt it? [File](keyed_xor.txt).
The key was created by taking two words from this [wordlist](wordlist.txt).

## Write-up
This challenge was one of the harder challenges in this CTF but once you understand the logic, the challenge can be broken down into two parts, each for finding the both words. The first part in this is to understand that our flag has a standard format of `easyctf{xxxx}`, thus, we can take advantage of the two-way XOR encryption to look for the first word first.

By encrypting our _encrypted_ data with a cycled key of `easyctf{`, we get

    # ./xor.py 
    drivell

Looking it up in the wordlist, we get the word `drivelling`. Wonderful, we've essentially square-rooted our time to solve this challenge and thus we can move on to quickly guessing our second word. This part is easily solved with attention, tenacity and [scripting](solve.py).

    # ./solve.py 
    easyctf{flagflagflagflagswrugdyiitwsfffyjjmdysukuiqdoqrxzamyhbbhboyfiesoyu}

Therefore, the flag is `easyctf{flagflagflagflagswrugdyiitwsfffyjjmdysukuiqdoqrxzamyhbbhboyfiesoyu}`.
