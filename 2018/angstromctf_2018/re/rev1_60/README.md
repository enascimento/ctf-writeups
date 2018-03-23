# AngstromCTF_2018: Rev1

**Category:** Reverse
**Points:** 60
**Description:**

>One of the commmon categories in CTFs is Reverse Engineering, which involves using a dissassembler and other tools to figure out how an executable file works. For your first real reversing challenge, here is an ELF file. Head over to `/problems/rev1/` on the shell server to try it out, and once you have the input right, get the flag!

## Write-up
Another simple challenge that can be solved with `strings`,

    $ strings rev1_32
    [...]
    [^_]
    Welcome to your first Reverse Engineering challenge!
    What is the password to this file? Enter password here: 
    s3cret_pa55word
    Sorry, the password isn't %s. Try again!
    Correct! You read my mind, have a flag: 
    [...]

With the password, we can now get the flag

    $ ./rev1_32
    Welcome to your first Reverse Engineering challenge!
    What is the password to this file? Enter password here: s3cret_pa55word
    Correct! You read my mind, have a flag: 
    actf{r3v_is_just_gettin_started!}

Therefore, the flag is `actf{r3v_is_just_gettin_started!}`.
