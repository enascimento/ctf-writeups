# GryphonCTF_2016: pr0_5k473r

**Category:** Crypto
**Points:** 10
**Description:**

>pr05k473r1337 is so cool! He grinded 5 railings in a row!
Creator - Darren Ang (@Southzxc)

## Write-up
We are given a [text file](ciphertext.txt). Inside it, we have `Gp7nnCm7py0_3cTuym__7f3Fh_u57h_}{d43`. To get the flag, you need to take a look at the description and we know that it's `5 railings`. Immediately, think of the `Railfence` cipher. We know it's 5 rows, thus we ge this.

    Gp7nnCm7py0_3cTuym__7f3Fh_u57h_}{d43

    G       p       7       n       n   
     C     m 7     p y     0 _     3 c  
      T   u   y   m   _   _   7   f   3 
       F h     _ u     5 7     h _     }
        {       d       4       3       

Therefore, the flag is `GCTF{hump7y_dump7y_547_0n_7h3_f3nc3}`.
