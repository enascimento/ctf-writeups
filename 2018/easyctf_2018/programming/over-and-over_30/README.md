# EasyCTF_2018: Over and Over

**Category:** Programming
**Points:** 30
**Description:**

>over and over and over and over and over and ...
Given a number `N`, print the string "over [and over]" such that the string contains `N` "over"s. There should not be newlines in the string.
For example:
For `N` = 1, print "over".
For `N` = 5, print "over and over and over and over and over".
For Python, consider using `for` and `range`.
For Java/CXX, consider using a `for` loop.
Try doing it with `while` too for practice!

## Write-up
[Dead simple challenge](solve.py),

    times=int(input())
    output=""
    for i in range(times):
        output+="over and "
    print(output.strip("and "))

Therefore, there is no flag.
