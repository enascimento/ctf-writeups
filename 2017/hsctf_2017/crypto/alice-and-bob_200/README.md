# HSCTF_2017: Alice and Bob

**Category:** Crypto
**Points:** 200
**Description:**

>Keith is sitting at home minding other people's business, and tracking conversations between two of their friends, Alice and Bob. However, Alice and Bob aren't real friends of theirs, and Keith has figured out that there is a secret number that Alice and Bob know, but refuse to tell Keith. So, Keith has kept track of the brief conversation between Alice and Bob. Using this transcript, help Keith find out the number that Alice and Bob are keeping to themselves.
Alice: Hey Bob! Let's use 987 as our base, and 8911991767204557841 as our prime modulus!
Bob: Aren't those numbers too small?
Alice: I hope not.
Bob: Ok! In that case my public key is 1317032838957486192.
Alice: Mine is 731665363559374475. 

## Write-up
This challenge was much easier solved by iterating upwards rather than by using the BSGS algorithm.

[Solution](solve.py)

    $ ./solve.py 
    a: 1213832
    b: 1201905
    K: 1715359156632385906

Therefore, the flag is `1715359156632385906`.