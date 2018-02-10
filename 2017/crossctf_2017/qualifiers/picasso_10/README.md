# CrossCTF_2017: Picasso

**Category:** Misc
**Points:** 10
**Description:**

>Picasso was a pretty good painter. But was he a good coder?
[File here](flag.png)

## Write-up
We get a file that is primarily comprised of a single line of pixels, comprised of different lengths of pixels. Maybe we can count the number of similar pixels before it changes and take it's character representation?

[Solution](solve.py)

    $ ./solve.py 
    CrossCTF{175_P13T_N07_P1C@SS0}

Therefore, the flag is `CrossCTF{175_P13T_N07_P1C@SS0}`.