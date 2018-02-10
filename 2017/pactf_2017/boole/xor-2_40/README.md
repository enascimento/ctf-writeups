# PACTF_2017: XOR 2

**Category:**
**Points:** 40
**Description:**

>Miles just sent me a really cool article to read! Unfortunately, he encrypted it before he sent it to me. Can you crack the code for me so I can read the article? [Article.txt](Article.txt).

**Hint:**

>Did you know that in typical English writing, a character is the same as the one k characters in front of it about 8% of the time, regardless of k?

## Write-up
A hint of repeated XOR, done easily through [XORTool](https://github.com/hellman/xortool).

    $ xortool -x -b -m 1000 Article.txt
    $ grep -R 'flag' -i xortool_out/
    Binary file xortool_out//000.out matches
    xortool_out//032.out:There are infinitely many even numbers, too, but they re much more common: exactly 500 out of the first 1,000. In fact, it s pretty apparent that out of the first X numbers, just about (1/2)X will be even. The flag is primes_are_cool.

Therefore, the flag is `primes_are_cool`.