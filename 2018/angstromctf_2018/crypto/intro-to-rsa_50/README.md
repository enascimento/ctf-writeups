# AngstromCTF_2018: Intro To RSA

**Category:** Crypto
**Points:** 50
**Description:**

>One common method of public key encryption is the RSA algorithm. Given p, q, e, and c, see if you can recover the message and find the flag!

## Write-up
Using Python, we can decrypt c with a [script](solve.py)!

    # Calculate n
    n = p * q

    # Calculate decryption keys
    phi = (p-1) * (q-1)
    d = gmpy2.invert(e, phi)

    # Decrypt flag
    m = int(pow(c, d, n))
    print(binascii.unhexlify(hex(m)[2:]).decode())

With the script, we can now get our flag.

    # ./solve.py 
    actf{rsa_is_reallllly_fun!!!!!!}

Therefore, the flag is `actf{rsa_is_reallllly_fun!!!!!!}`.
