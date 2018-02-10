# CrossCTF_2017:

**Category:** Reverse Engineering
**Points:** 25
**Description:**

>Can you unravel the flag? [File here](scrackme)

## Write-up
Loading it up in something like Hopper, we get a pretty good glimpse of what we need to do, so we have to find the payload. Firstly, `bastion` leads us to another pointer where we find our real payload, save for one character, which if we look further in ASM, we find `0x69` in `crackme()`. Therefore, the full payload is `692A583744377420661D5C32066A132617791E41355D6E314236027647245953`, knowing that, we can xor every byte of the payload with the next byte to give us the flag.

    0x69 ^ 0x2a = C
    0x2a ^ 0x58 = r
    ...

Therefore, the flag is `CrossCTF{An4ly51ng_th3_st4t1c}`.