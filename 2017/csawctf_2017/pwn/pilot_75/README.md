# CSAWCTF_2017: Pilot

**Category:** Pwn
**Points:** 75
**Description:**

>Can I take your order
nc pwn.chal.csaw.io 8464
16:05 Eastern: Updated binary

## Write-up
This challenge is a standard buffer overflow, return to shellcode exploit, where the address is fed to you. This is made even simpler through [Python](solve.py).

    # ./solve.py 
    [+] Opening connection to pwn.chal.csaw.io on port 8464: Done
    [*] Switching to interactive mode
    [*]Command:
    $ ls
    flag
    pilot
    $ cat flag
    flag{1nput_c00rd1nat3s_Strap_y0urse1v3s_1n_b0ys}

Therefore, the flag is `flag{1nput_c00rd1nat3s_Strap_y0urse1v3s_1n_b0ys}`.
