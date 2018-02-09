# GryphonCTF_2016: Jack and the Beanstalk
**Category:** Cryptography
**Points:** 20
**Description:**

>Jack is giving away free magical beans!
Play it here: nc play.spgame.site 9999
Creator - Kelvin Neo (@deathline75)

**Hint:**

>Jack planted seeds already. Jack also owns 2 pythons

## Write-up
DISCLAIMER: This write-up for this challenge is a painful one.

This time around, we are given a challenge where we have to guess the next number, consecutively for 10 times. Firstly, I tried running a bruteforce script to open and reopen connections to generate a list of numbers and what follows behind that number. This is similar to neural networking, in particular something called [Markov Chain](https://en.wikipedia.org/wiki/Markov_chain).

I then extended the chain to something around 7 integers long but it was not possible to get up to 10 times correct. So, that brings us back to square one. If the bruteforce method doesn't work, it means the numbers generated are completely random, or is it?

Looking back at the question hint, we see that 'Jack' has planted the seeds already. Additionally, Jack also owns 2 pythons. If we take it literally, we won't understand anything but since this challenge is under cryptography and that we are supposed to guess the next number, we can take it to heart that this is, in fact, a RNG.

Looking at the hint again, '2 pythons' could mean Python language and 'planted seeds' could mean that the RNG has been seeded already. Knowing that, we can devise a simple script to test it.

    #! /usr/bin/env python
    ##
    import socket
    import re
    import random

    s = socket.socket()
    s.connect(('play.spgame.site', 9999))
    r = random.Random()

    while True:
        data = s.recv(4096)
        if data != "":
            print("RECV>>>" + data.strip())
            if "number is" in data:
                try:
                    number = int(re.findall('[0-9]+', data)[1])
                except IndexError:
                    number = int(re.findall('[0-9]+', data)[0])

                r.seed(number)
                s.send(str(r.randint(1, 100)) + "\n")

Running the script gives us,

    $ ./test.py 
    RECV>>>My numbers are always between 1 (inclusive) to 100 (inclusive)!
    RECV>>>Guess my number 10 times and you get a prize!
    My number is: 95
    Guess my next number: 
    RECV>>>Well done!
    RECV>>>My number is: 52
    Guess my next number: 
    RECV>>>Oh no! That's not my number!

Running the script multiple times changes nothing, with the first number being an automatic success. So, what's going on? Well, after hours of constant testing different combinations like seeding the random number generator with the sum of the new number and the previous number, the new number with an exponent of the previous number and approximately 100 (slightly exaggerated) other combinations. That still yielded nothing.

So, new plan, this time around, I took the first number, seeded with ONLY the first number and just echo out the randint(1, 100).

    #! /usr/bin/env python
    ##
    import socket
    import re
    import random

    s = socket.socket()
    s.connect(('play.spgame.site', 9999))
    r = random.Random()
    seeded = False

    while True:
        data = s.recv(4096)
        if data != "":
            print("RECV>>>" + data.strip())
            if "number is" in data:
                try:
                    number = int(re.findall('[0-9]+', data)[1])
                except IndexError:
                    number = int(re.findall('[0-9]+', data)[0])

                if not seeded:
                    r.seed(number)
                    seeded = not seeded

                response = str(r.randint(1, 100)) + "\n"
                print(response)
                s.send(response)


Amazingly, this happened.

    $ ./test.py
    RECV>>>My numbers are always between 1 (inclusive) to 100 (inclusive)!
    RECV>>>Guess my number 10 times and you get a prize!
    My number is: 3
    Guess my next number: 
    24
    RECV>>>Well done!
    RECV>>>My number is: 55
    Guess my next number: 
    55
    RECV>>>Oh no! That's not my number!

Do you see it? My next number guess for number 2 also happens to be the 2nd number! Repeating the script returns the same thing,

    RECV>>>My number is: 56
    Guess my next number: 
    56

We might be on to something here. Now I try to make it the random number generator dump an integer off. As it appears, the number we get from the server is every alternate number, so we just have to dump one integer off to get the correct next guess.

    if not seeded:
        r.seed(number)
        seeded = not seeded

    response = str(r.randint(1, 100)) + "\n"
    r.randint(1, 100)
    print(response)
    s.send(response)

Viola!

    $ ./test.py 
    RECV>>>My numbers are always between 1 (inclusive) to 100 (inclusive)!
    RECV>>>Guess my number 10 times and you get a prize!
    My number is: 5
    Guess my next number: 
    63
    RECV>>>Well done!
    RECV>>>My number is: 75
    Guess my next number: 
    80
    RECV>>>Well done!
    RECV>>>My number is: 95
    Guess my next number: 
    74
    RECV>>>Well done!
    RECV>>>My number is: 93
    Guess my next number: 
    3
    RECV>>>Well done!
    RECV>>>My number is: 47
    Guess my next number: 
    95
    RECV>>>Well done!
    RECV>>>My number is: 65
    Guess my next number: 
    91
    RECV>>>Well done!
    RECV>>>My number is: 12
    Guess my next number: 
    47
    RECV>>>Well done!
    RECV>>>My number is: 25
    Guess my next number: 
    55
    RECV>>>Well done!
    RECV>>>My number is: 58
    Guess my next number: 
    2
    RECV>>>Well done!
    RECV>>>My number is: 22
    Guess my next number: 
    28
    RECV>>>Well done!
    RECV>>>This is my prize to you: GCTF{RNG_g@m3_700_str0nk}

Therefore, the flag is `GCTF{RNG_g@m3_700_str0nk}`. [Script to automatically and beautifully crack this challenge linked here.](script.py)


