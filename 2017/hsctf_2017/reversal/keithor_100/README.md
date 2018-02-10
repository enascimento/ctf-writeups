# HSCTF_2017:

**Category:** Reversal
**Points:** 100
**Description:**

>[Too many hashes](keithor.py). Help Keith get to the flag! 

## Write-up
Just b64decode it to hex encoding, get the md5 hash and run it against hashkiller.

    $ ./solve.py 
    MD5 of Flag: 4f79807a7c47f697bd5f06beef955cfd
    SHA1 of Flag: f4fdaef8ade8edf707858fe4294d780d69d4d6a8
    Flag: TlZMN09

Therefore, the flag is `TlZMN09`.