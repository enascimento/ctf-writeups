# EasyCTF_2018: Not OTP

**Category:** Cryptography
**Points:** 100
**Description:**

>It seems we've intercepted 2 strings that were both encrypted with what looks like OTP! Is it possible to decrypt them? [file](ciphered.txt)

## Write-up
This challenge was physically and mentally the worst of all challenges. Essentially, the OTP used has been used twice. By XOR-ing both strings together, we effectively remove the presence of the OTP key. So, to decrypt the message, we need to do [dragcribbing using a tool](https://github.com/SpiderLabs/cribdrag).

The hardest part about this challenge is guessing that `crib` was in reference to `cribbing` in reference to `Known-Plaintext Attack`. Other than that, this challenge is essentially a guessing game.

    # ./cribdrag.py 0b071b0512440400024106001614001d06490448001048540a04421a00105216184516045c493a0f450d4802154e590e195318491e09460b1756111d00065516121e514c034c0e0100191f410c0f071c1b00460e1c11147f1d1a503c0c1654002d01135f0e141a

    Your message is currently:
    0   hurgadergaderg this is the secret string
    40   that you will never guess! flag is easy
    80  ctf{otp_ttp_cr1b_dr4gz}
    Your key is currently:
    0   cribs are beds in which babies sleep. Th
    40  ey can also refer to a sample of plainte
    80  xt used in codebreaking

Therefore, the flag is `easyctf{otp_ttp_cr1b_dr4gz}`.
