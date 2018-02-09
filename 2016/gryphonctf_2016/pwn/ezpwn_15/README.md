# GryphonCTF_2016:

**Category:** Pwn
**Points:** 15
**Description:**

>I just learned C last semester! Better put that to the test!
Play it here: nc play.spgame.site 9993
Creator - Kelvin Neo (@deathline75)

## Write-up

**_Credits to @zst123 [Manzel Seet] for helping with the general idea of this challenge. (OS duplication all me though)._**

We are given a [source code for the calculator](calculator.c). On first look, it seems fairly simple, we just need to guess the random number and come up with integer sums to overflow into the negative. As we know, general unsigned 32 bit integers go from `0` to `2^32 - 1` and signed 32 bit integers go from `-2^31` to `2^31 - 1`. To overflow from `0` to negative `-100`, you need to add `2^32 - 1 - 100`, or to effectively add `4,294,967,195`. 

This challenge however, tests much more on a deeper topic, on C's `rand()` and `srand()` function. If we take a look at the source code,

    srand(time(NULL));
    ...
    int j =  rand() % 12345678 * -1;
    int r = j + 0;

We see that the secret number is `rand()` for an integer between `0` and `-12345678` and we also see that `srand(time(NULL))` seeds the random number generator with the timestamp.

Attempting to create a [similar program](get_magic.c), we find that somehow, the secret number in our [script](script.py) doesn't seem to correspond to the number in the server... what now? Well, apparently, C `rand()` function [differs from OS to OS](https://stackoverflow.com/questions/11567613/different-random-number-generation-between-os). If running the program on a MacBook OSX doesn't work, we can try... Ubuntu.

And thus, God said, let there be [Dockerfile](Dockerfile).

    $ docker run --rm ezpwn
    Traceback (most recent call last):
      File "./script.py", line 38, in <module>
        raise Exception('GCTF FLAG FOUND %s' % data)
    Exception: GCTF FLAG FOUND 
    Here is your prize GCTF{5ub7r4c710n_by_h1dd3n_4dd1710n}!

Therefore, the flag is `GCTF{5ub7r4c710n_by_h1dd3n_4dd1710n}`.
