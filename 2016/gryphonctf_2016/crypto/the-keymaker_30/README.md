# GryphonCTF_2016: The Keymaker

**Category:** Crypto
**Points:** 30
**Description:**

>You've intercepted an encrypted flag that was being transmitted between two GCTF admins, along with a 256-bit RSA public key that was used in the encryption of the flag...
Creator - Shawn Pang (@Optixal)

## Write-up
**_DISCLAIMER: TOOLS WERE USED, CREDITS TO @Ganapati ON GITHUB_**

Okay, this around, we are given a [ciphertext](flag_ciphertext) and a [public key](pub_key.txt). It appears that the public key happens to be a short, 256-bit RSA key and thus we can search up ways to break RSA keys. As most people reading this should know, current standards of RSA keys are currently at 2048-4096 bits and bitsizes of below 2048 should never be used.

Since we have a 256-bit key, we can take advantage of a well-known exploit on the RSA algorithm known as the [Wiener's attack](https://en.wikipedia.org/wiki/Wiener%27s_attack). As of this writing, I'm no expert in cryptography but what I do have are skills in Google. Googling, to be exact, led me to a certain [git repository](https://github.com/Ganapati/RsaCtfTool). Simple enough, downloading it and running,

    ./RsaCtfTool.py --publickey ~/Downloads/pub_key.txt --uncipher ~/Downloads/flag_ciphertext 
    Clear text : GCTF{1f_0nly_17_w45_1n_1337}

Voila!~ Therefore, the flag is `GCTF{1f_0nly_17_w45_1n_1337}`.

P.S On hindsight, I probably could've tried to make my own script knowing the algorithms, too lazy.
