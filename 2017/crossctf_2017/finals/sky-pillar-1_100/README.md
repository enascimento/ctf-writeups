# CrossCTF_2017: Sky Pillar 1

**Category:** Reverse Engineering
**Points:** 100
**Description:**

>192.168.0.31:1350 [File here](skypillar)

## Write-up
Looking in `levelone()`, we find our hex-encoded passphrase in little endian, so we need to deal with that.

    0x40772049
    0x20406e6e
    0x74206562
    0x76206568
    0x20797265
    0x74736562

    V

    49207740
    6e6e4020
    62652074
    68652076
    65727920
    62657374

Decoding it yields `I w@nn@ be the very best`. Entering it into the server gives us the flag.

    $ ./skypillar
                                     Welcome to                                    
     ______     __  __     __  __        ______   __     __         __         ______     ______
    /\  ___\   /\ \/ /    /\ \_\ \      /\  == \ /\ \   /\ \       /\ \       /\  __ \   /\  == \
    \ \___  \  \ \  _"-.  \ \____ \     \ \  _-/ \ \ \  \ \ \____  \ \ \____  \ \  __ \  \ \  __<
     \/\_____\  \ \_\ \_\  \/\_____\     \ \_\    \ \_\  \ \_____\  \ \_____\  \ \_\ \_\  \ \_\ \_\
      \/_____/   \/_/\/_/   \/_____/      \/_/     \/_/   \/_____/   \/_____/   \/_/\/_/   \/_/ /_/
    ================================================================================
                        Home of the legendary Pokemon, Rayquaza                          
    ================================================================================
    There are 5 Levels to climb. Each level requires a specifc code to unlock the next level.
    Your goal is to reach the top, and catch the legendary Rayquaza... Good luck!
    ====================================================================
                              LEVEL 01                                  
    ====================================================================
    Enter code: I w@nn@ be the very best
    CrossCTF{xxxxxxxxxxxxxxxxx}

Therefore, the flag is ``.
