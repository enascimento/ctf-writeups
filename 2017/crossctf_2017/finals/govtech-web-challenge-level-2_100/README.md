# CrossCTF_2017: GovTech Web Challenge Level 2

**Category:** Web
**Points:** 100
**Description:**

>This is a game of Tic-Tac-Toe. There are some messages encoded in Tic-Tac-Toe format. Please help us decipher it! [Challenge here](http://govtech-challenge.com/challenge/)

## Write-up
This challenge has to be done after level 1, since you need to use the flag from the first one as the passphrase for level 2.

The clues given as using XOR to derive the hexadecimal ASCII representation of the flag. As we are given 12 pairs of tic-tac-toe tables, we can derive the length of the flag, which is 12. Additionally, from correctly trying to parse the puzzle, we actually arrive at an incorrect flag.

    47 6f 76 54 65 63 68 7b 41 46 43 7d
    GovTech{AFC}

As such, what our team decided to do, is the bruteforce the `26^3` possiblities of the flag, which turned out to be `GovTech{ABC}`.

Therefore, the flag is `GovTech{ABC}`.
