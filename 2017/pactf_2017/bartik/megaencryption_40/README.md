# PACTF_2017: MegaEncryption (TM)

**Category:**
**Points:** 40
**Description:**

>Personal Advancement of Cuil Therory Foundation
The Personal Advancement of Cuil Therory Foundation (PACTF) left a message for Tony, but they used MegaEncryption (TM) to encrypt it. What did they say? Should we be worried? It seems like they used some sort of public medium to send the message

**Hint:**

>They kept records!

## Write-up
Irritating, truly this challenge, requires us to go search up [discussion history](https://en.wikipedia.org/w/index.php?title=User_talk:Tony_Tan&oldid=770856430). Afterwards, a intense `base64 -d` chain.

    $ cat ciphertext.txt | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d 
    Oh my goodness! It's gotten so bad. The cuils are rising... they want to outlaw encryption... I'd rate their world +200 Cuils! At least I have MegaEncryption (TM) to keep me safe. the_cuil_is_too_much_to_handle

Therefore, the flag is `the_cuil_is_too_much_to_handle`.