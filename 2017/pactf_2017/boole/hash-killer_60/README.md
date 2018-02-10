# PACTF_2017: Hash Killer

**Category:**
**Points:** 60
**Description:**

>Qu’est que c’est?
We were clearing out the old server and came across a really weird file…

**Hint:**

>Did someone say MD5? And that last line seems different from the rest…

## Write-up
Firstly, all the lines except the last one can be cracked as MD5, returning us [decoded_hashes.txt](decoded_hashes.txt). Looks like we have a hint regarding the last line, let's see.

    8fc42c6ddf9966db3b09e84365034357 MD5 : the
    c47d187067c6cf953245f128b5fde62a MD5 : word
    424149e499a7cb738810dc0e537c8490 MD5 : 'AES'
    0800fc577294c34e0b28ad2839435945 MD5 : hash
    a2a551a6458a8de22446cc76d639a9e9 MD5 : is
    8fc42c6ddf9966db3b09e84365034357 MD5 : the
    3c6e0b8a9c15224a8228b9a98ca1531d MD5 : key

`AES` md5summed returns `76b7593457e2ab50befe2dcd63cf388f`. Let's try making a [Pythonic decrypter](solve.py).

    $ ./solve.py 
    flag{w3_l0v3_3ncrypt10n}
    
Therefore, the flag is `flag{w3_l0v3_3ncrypt10n}`.