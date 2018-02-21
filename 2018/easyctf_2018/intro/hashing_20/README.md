# EasyCTF_2018: Hashing

**Category:** Intro
**Points:** 20
**Description:**

>Cryptographic hashes are pretty cool! Take the SHA-512 hash of this file, and submit it as your flag.

## Write-up
Really simple too, just use `sha512sum` on Linux,

    # sha512sum sha512.png 
    418a53d3e4c8239d7c861ad2836e4b6b4488a8ef3327b4783e42b7f074d414f5a95e7db14ebe5177354ec58dadb5377e5248fda3b9a11edc8362b58a5c38d896  sha512.png

Therefore, the flag is `418a53d3e4c8239d7c861ad2836e4b6b4488a8ef3327b4783e42b7f074d414f5a95e7db14ebe5177354ec58dadb5377e5248fda3b9a11edc8362b58a5c38d896`.
