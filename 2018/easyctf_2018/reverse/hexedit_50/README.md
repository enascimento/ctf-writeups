# EasyCTF_2018: hexedit

**Category:** Reverse Engineering
**Points:** 50
**Description:**

>Can you find the flag in this [file](hexedit)?

## Write-up
Another simple one, just using `$ strings`.

    root@ctf:~/downloads# strings hexedit
    [...]
    []A\A]A^A_
    Find the flag!
    ;*3$"
    easyctf{c20f2b9f}
    GCC: (Ubuntu 4.8.4-2ubuntu1~14.04.3) 4.8.4
    .symtab
    .strtab
    .shstrtab
    [...]

Therefore, the flag is `easyctf{c20f2b9f}`.
