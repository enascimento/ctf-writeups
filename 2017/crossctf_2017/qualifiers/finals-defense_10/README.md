# CrossCTF_2017: Finals Defense

**Category:** Finals
**Points:** 10
**Description:**

>Time to practice for the finals! Patch the binary so that the flag can't be printed. Remember to test it locally first with the following command!
while true;do 
nc -l -p 9001 -e ./one 
done; 
[File here](one)

## Write-up
An easy patching, just change the instructions at `flag` to `leave` & `ret`. Too bad they don't check the [binary](one_patched) thoroughly. LOL.

Therefore, the flag is `CrossCTF{P@TCHING_IZ_E@SY}`.