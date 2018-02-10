# CrossCTF_2017: Close Friends

**Category:** Cryptography
**Points:** 20
**Description:**

>Alice and Bob are very close friends.
They share their secrets with each other and they do not want others to intercept it.
So they decided to implement [their own RSA](generate.py) to encrypt their messages.
[File here](output.txt)

## Write-up
This is a Fermat's RSA attack challenge requiring us to use it's functions. Only doable in [python](solve.py)

    $ ./solve.py 
    Flag: CrossCTF{its_g00d_t0_hav3_c1o5e_friend5_i5nt_it}

Therefore, the flag is `CrossCTF{its_g00d_t0_hav3_c1o5e_friend5_i5nt_it}`.