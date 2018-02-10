# CrossCTF_2017: GovTech Binary Challenge Level 2

**Category:** Binary
**Points:** 100
**Description:**

>There's more!
[File here](../govtech-binary-challenge-level-1_75/dist.zip).

## Write-up
Utilizing the same binary as level 1, this can be solved through incorporating the usage of `NothingImportant.class` through the usage of an external `.java` class. However, this will take a long time and it's more efficient to transpile the code to remove all the sleep delays.

As such, I've come to use the `hashlib` library in Python for [ultra-efficient solving code](solve.py).
