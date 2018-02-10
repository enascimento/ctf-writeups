# PACTF_2017: Exploring The Binary

**Category:**
**Points:** 10
**Description:**

>Why doesn’t this [file](a.out) print!! Did I forget to put in the print statement when I compiled?

**Hint:**

>

## Write-up
Preliminary testings immediately gave me the flag. Huh.

    $ strings /Users/Amos/Repositories/pactf_2017_writeup/boole/exploring-the-binary/a.out | grep flag
    flag_1297831859

Therefore, the flag is `flag_1297831859`.