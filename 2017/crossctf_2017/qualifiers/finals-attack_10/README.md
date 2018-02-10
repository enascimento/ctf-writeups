# CrossCTF_2017: Finals Attack

**Category:** Finals
**Points:** 10
**Description:**

>Time to practice for the finals! Write a python script that exploits the target at the domain 'challenge_runner'. Remember to test it locally first with the following command!
    while true;do 
    nc -l -p 9001 -e ./one 
    done; 
[File here](one)

## Write-up
A really simple one, considering that the binary was buffer overflowable, we just have to do the same here for attacking.

[Solution](solve.py)

Instead of running this, upload it into the server to get the flag.

Therefore, the flag is `CrossCTF{EXPL01T1NG_M3_1Z_H@RD}`.