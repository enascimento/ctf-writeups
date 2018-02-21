# EasyCTF_2018: Zipperoni

**Category:** Miscellanous
**Points:** 160
**Description:**

>I've created a dastardly chain of [zip files](zip_files.tar). Now you'll never find my flag!
The first file is `begin.zip`, with password `coolkarni`.

## Write-up
This challenge is just a programming challenge with continous zip and bruteforcing. However, traditional bruteforcing will take too long and instead you have to be smart when bruteforcing. Firstly, the pattern given in `begin.zip` goes along the lines of something like `___0_0_`. Well, essentially, the `_`s are part of the actual password but `0` refers to digits.

    0 -> 0123456789
    a -> abcdefghijklmnopqrstuvwxyz
    A -> ABCDEFGHIJKLMNOPQRSTUVWXYZ

So, to solve this, we need to be good with [Python](solve.py) scripting :) Additionally, the `hash.txt` file that is produced every iteration is the SHA-1 hash of the password needed for the next zip file specified in `filename.txt`.

    $ ./solve.py 
    ATTEMPTING: __0_0_
    SUCCESS: __1_8_
    [...]
    ATTEMPTING: _00aA0
    SUCCESS: _46rW9
    easyctf{you_must_REALLY_luv_zip_files_by_now!}

Therefore, the flag is `easyctf{you_must_REALLY_luv_zip_files_by_now!}`
