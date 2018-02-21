# EasyCTF_2018: Flag Time

**Category:** Misc
**Points:** 80
**Description:**

>This problem is so easy, it can be solved in a matter of seconds. Port 12482.

## Write-up
This challenge was mentally the worst ever, since I originally used a single-threaded script to do it but with 1 second delays per correct character, I would have taken a millienia to solve this. Enter the multi-threaded scripts.

Essentially, this challenge is a timing attack challenge, except the timing delay is 1 second long and is immensely painful. I finally decided to use my favourite threads to solve this challenge in hopes of being able to sleep at night. [Full script available here](solve.py).

    # ./solve.py
    [...]
    [*] Current Best: 'easyctf{ez_t1m1ng_4ttack!}' Attempting: 'easyctf{ez_t1m1ng_4ttack!}@' Time: 26.31693387031555
    [*] Current Best: 'easyctf{ez_t1m1ng_4ttack!}' Attempting: 'easyctf{ez_t1m1ng_4ttack!}<' Time: 26.315574884414673
    [*] Current Best: 'easyctf{ez_t1m1ng_4ttack!}' Attempting: 'easyctf{ez_t1m1ng_4ttack!}?' Time: 26.317901134490967
    [*] Current Best: 'easyctf{ez_t1m1ng_4ttack!}' Attempting: 'easyctf{ez_t1m1ng_4ttack!}=' Time: 26.330061674118042
    [*] Current Best: 'easyctf{ez_t1m1ng_4ttack!}' Attempting: 'easyctf{ez_t1m1ng_4ttack!}~' Time: 26.31587290763855
    [+] Flag Found! easyctf{ez_t1m1ng_4ttack!}

Therefore, the flag is `easyctf{ez_t1m1ng_4ttack!}`.
