# CrossCTF_2017: Sky Pillar 4

**Category:** Reverse Engineering
**Points:** 300
**Description:**

>192.168.0.31:1350 Please start from level 01

## Write-up
This one was the pinnacle of my reverse engineering skill. With a little luck, you would guess that this is related to Fibonacci numbers, unfortunately, I did not in time for competition, so I just transpiled everything into [solve.c](solve.c).

    $ gcc solve.c && ./a.out 
    Currently on 584
    Found! 584
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
    ====================================================================
                              LEVEL 03                                  
    ====================================================================
    Enter Code: 0 @ C D G
    CrossCTF{xxxxxxxxxxxxxxxxx}
    ====================================================================
                              LEVEL 04                                  
    ====================================================================
    Enter Code: 584
    CrossCTF{xxxxxxxxxxxxxxxxx}

Therefore, the flag is ``.
