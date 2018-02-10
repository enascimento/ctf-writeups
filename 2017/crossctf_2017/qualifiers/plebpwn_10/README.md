# CrossCTF_2017: Plebpwn

**Category:** Pwn
**Points:** 10
**Description:**

>Please pwn my plebian password program!
Please connect to 128.199.98.78:1700 
[File here](plebpwn)

## Write-up
A case of a buffer overflow attack though not obvious. Firstly, analysing the executable tells us that the buffer is `0x40` bytes long but the `read()` reads in `0x80` bytes. Trying to overflow `0x80` bytes crashes the application due to the overwriting of address of a string resulting in it crashing due to being unable to read from a location.

[Solution](solve.py)

Therefore, the flag is `CrossCTF{av01d_th0s3_cr4sh3s}`.