# HSCTF_2017: Coin Flip

**Category:** Algo
**Points:** 100
**Description:**

>Keith has been very bored with his job as an industrial couponer lately, and so he has decided to spend his time flipping coins. The results of his coin flips are [in this file](file.txt). Keith now wants to know how many runs of flips he found. A run is any consecutive sequence of the same flip. For example, the flips 001111101011 have three runs of length one, two runs of length two, and one run of length five. Can you help Keith count runs? The flag is the number of runs of length one, the number of runs of length two, the number of runs of length three, etc. up to the longest run in the sequence, each separated by a comma and a space. 

## Write-up
Just remember to count the last bit.

[Solution](solve.py)

Therefore, the flag is `249368, 124813, 62558, 31388, 15476, 7891, 3975, 1982, 943, 486, 270, 107, 64, 33, 15, 8, 4, 1, 1, 1`.