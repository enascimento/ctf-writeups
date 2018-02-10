# CSAWCTF_2017: Baby_Crypt

**Category:** Crypto
**Points:** 350
**Description:**

>The cookie is input + flag AES ECB encrypted with the sha256 of the flag as the key.
nc crypto.chal.csaw.io 1578

## Write-up
A challenge based on the block-like behaviour of ECB. This one tests upon how ECB can be exploited if you can control part of the input. For example, in the following example, each block is encrypted separately, so if both blocks are the same, they produce the same ciphertext.

    [INPUT 32] | [FLAG 32] 
    012356789  | 0123456789

    Therefore, INPUT == FLAG.

Now, this can be exploited if we pad the flag out to where we only need to bruteforce one. In the following example, we can simply bruteforce the last character of the first block, till the first and second blocks of ciphertext is the same, concluding we've broken the first letter of the flag. This can then be rinsed and repeated! This is lovingly automated with [Python](solve.py)!

    0000000X | 0000000[FIRST LETTER OF FLAG] | [REST OF FLAG]
    000000fX | 000000f[SECOND LETTER OF FLAG] | [REST OF FLAG]
    00000flX | 00000fl[THIRD LETTER OF FLAG] | [REST OF FLAG]
    ...

Running the script gives us,

    # ./solve.py 
    [+] Opening connection to crypto.chal.csaw.io on port 1578: Done
    [+] Cracking flag...: Done
    [+] flag{Crypt0_is_s0_h@rd_t0_d0...}
    [*] Closed connection to crypto.chal.csaw.io port 1578

Therefore, the flag is `flag{Crypt0_is_s0_h@rd_t0_d0...}`.
