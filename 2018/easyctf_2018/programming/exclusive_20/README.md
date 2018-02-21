# EasyCTF_2018: Exclusive

**Category:** Programming
**Points:** 30
**Description:**

>Given two integers a and b, return a xor b. Remember, the xor operator is a bitwise operator that's usually represented by the ^ character.
For example, if your input was 5 7, then you should print 2.

## Write-up
[Dead simple challenge](solve.py),

    ab = input().split(" ")
    print(int(ab[0]) ^ int(ab[1])) 

Therefore, there is no flag.
