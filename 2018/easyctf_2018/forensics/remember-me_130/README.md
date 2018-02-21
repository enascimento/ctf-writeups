# EasyCTF_2018: Remember Me

**Category:** Forensics
**Points:** 130
**Description:**

>I'm such a klutz! I know I hid a flag in [this file](scarboroughfair.mp3) somewhere, but I can't remember where I put it!
Song is from sukasuka.

## Write-up
Using Audacity, one can easily remove the vocals entirely from the given file through the **_Effect > Vocal Reduction and Isolation_** feature. After a bit of extracting, we are left with an [audio clip](scarboroughfair_solved.wav) of someone reading the flag out.

Therefore, the flag is `easyctf{4ud10_st3g}`.
