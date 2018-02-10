# HSCTF_2017: KE1TH

**Category:** Reversal
**Points:** 200
**Description:**

>Keith recently coded a [small authorization software](Keith.class) for his/her computer to hide personal files. Unfortunately, he/she hit his head and forgot his/her password. Now he/she must reverse engineer his/her software to regain his/her password. 

## Write-up
It's just a small reversing challenge where they already given everything we need. `IV`? Check. `Key`? Check. `Ciphertext`? Check.

[Solution](solve.py)

    $ ./solve.py 
    Flag: this_was_a_short_and_easy_problem_2B3F5AC0

Therefore, the flag is `this_was_a_short_and_easy_problem_2B3F5AC0`.