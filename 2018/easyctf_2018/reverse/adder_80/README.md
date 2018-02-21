# EasyCTF_2018: Adder

**Category:** Reverse Engineering
**Points:** 80
**Description:**

>This program adds numbers. Find the flag! [adder](adder)

## Write-up
This challenge is really simple, just load up the decompiler,

    │           0x00400b9c      01d0           add eax, edx
    │           0x00400b9e      3d39050000     cmp eax, 0x539              ; 1337
    │       ┌─< 0x00400ba3      7527           jne 0x400bcc

Add 3 numbers!

    # ./adder 
    Enter three numbers!
    0
    1000
    337
    easyctf{y0u_added_thr33_nums!}

Therefore, the flag is `easyctf{y0u_added_thr33_nums!}`.
