# EasyCTF_2018: Soupreme Encoder

**Category:** Crypto
**Points:** 20
**Description:**

>Decode this `68657869745f6d6174655f6662623461303034636232313632383661396231`

## Write-up
This challenge is also really simple after recognizing the presence of ASCII characters encoded in hexadecimal. As I'm a really fancy and posh person, I resort to using `rax2` from `radere2` to convert this but any hexadecimal to ASCII converter will do the same!

    root@ctf:~# rax2 -s 68657869745f6d6174655f6662623461303034636232313632383661396231
    hexit_mate_fbb4a004cb216286a9b1

Therefore, the flag is `hexit_mate_fbb4a004cb216286a9b1`.
