# AngstromCTF_2018: Back To Base - ICS

**Category:** Crypto
**Points:** 20
**Description:**

>Here at ångstromCTF, we know all the powers of two! Try and decode [this](problem.txt).

## Write-up
We get a file containing,

    Part 1: 011000010110001101110100011001100111101100110000011011100110010101011111011101000111011100110000010111110110011000110000
    Part 2: 165 162 137 145 151 147 150 164 137 163 151 170 164 63 63 
    Part 3: 6e5f7468317274797477305f733178
    Part 4: dHlmMHVyX25vX20wcmV9

    Flag is the concatenation of the four decoded parts.

Using any converter, particularly `rax2`, we get the following,

    root@ctf:~# rax2 -b 011000010110001101110100011001100111101100110000011011100110010101011111011101000111011100110000010111110110011000110000
    actf{0ne_tw0_f0

    root@ctf:~# rax2 165o 162o 137o 145o 151o 147o 150o 164o 137o 163o 151o 170o 164o 63o 63o | rax2 -s
    ur_eight_sixt33

    root@ctf:~# rax2 -s 6e5f7468317274797477305f733178
    n_th1rtytw0_s1x

    root@ctf:~# rax2 -D dHlmMHVyX25vX20wcmV9
    tyf0ur_no_m0re}

Therefore, the flag is `actf{0ne_tw0_f0ur_eight_sixt33n_th1rtytw0_s1xtyf0ur_no_m0re}`.
