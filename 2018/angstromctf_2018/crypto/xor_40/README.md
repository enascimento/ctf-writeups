# AngstromCTF_2018: 

**Category:** Crypto
**Points:** 40
**Description:**

>We found these [mysterious symbols](ciphertext.txt) hidden in ancient (1950s-era) ruins. We think a single byte may be key to unlocking the mystery. Can you help us figure out what they mean?

## Write-up
This is just a single-byte XOR encryption.

    import binascii

    ciphertext = binascii.unhexlify("fbf9eefce1f2f5eaffc5e3f5efc5efe9fffec5fbc5e9f9e8f3eaeee7")
    for key in range(255):
        plaintext = ""
        for c in ciphertext:
            plaintext += chr(c ^ key)
        if "ctf" in plaintext:
            print(plaintext)

In a script, we get our flag

    $ ./script.py
    actf{hope_you_used_a_script}

Therefore, the flag is `actf{hope_you_used_a_script}`.
