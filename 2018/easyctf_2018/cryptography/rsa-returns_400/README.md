# EasyCTF_2018: RSA Returns

**Category:** Cryptography
**Points:** 400
**Description:**

>It's the return of everyone's favorite cryptosystem! Crack it for another flag. Help me decipher [file](file).

## Write-up
This challenge reeks of ROCA and even signature checks confirmed it. However, there were no PoCs for ROCA. Instead, I came across [NECA](https://gitlab.com/jix/neca). I love open source.

    $ ./neca 8729581225262922855975327965201482091621603739716646047811615593091116970536029316597901441665882719811658068143200342813247447157083464709878924070575467
    NECA - Not Even Coppersmith's Attack
    ROCA weak RSA key attack by Jannis Harder (me@jix.one)

     *** Currently only 512-bit keys are supported ***

     *** OpenMP support enabled ***

    N = 8729581225262922855975327965201482091621603739716646047811615593091116970536029316597901441665882719811658068143200342813247447157083464709878924070575467
    Factoring...

     [=                       ]  5.40% elapsed: 92s left: 1610.35s total: 1702.36s

    Factorization found:
    N = 98156620780003086692513114529458599425385116396074158691207247964958060681783 * 88935225722861812850195157838313383408060631426601900565225384215559424240749

Now that we have our factors, just simply decrypt `c`

    $ ./solve.py 
    easyctf{kmwmv8wnhnap5old1p}

Therefore, the flag is `easyctf{kmwmv8wnhnap5old1p}`.
