# PACTF_2017: Zeroes and Ones

**Category:**
**Points:** 30
**Description:**

>Bit String Flicking
How many solutions are there for X in the expression:
LCIRC -3 (01011 AND X OR 10100) = 01101

**Hint:**

>Try simplifying it?

## Write-up
Simplification of strings!

    LCIRC -3 (01011 AND X OR 10100) = 01101

Since LCIRC refers to circulating bits to the left, we have to recirculate to the right by 3.

    (01011 AND X OR 10100) = 10101

Now, to solve for permutations of x, we need to see which bits can be changed without affected the results.

    (01011 AND XXXXX OR 10100) = 10101
               ^ ^ 

As two bits can be changed, total solutions equals `2*2`

Therefore, the flag is `4`.