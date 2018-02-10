# CrossCTF_2017:

**Category:** Misc
**Points:** 5
**Description:**

>We have intercepted secret messages but it seems like AAAAAAAAAAA to us. Can you help us?
[File here](flag.png)

## Write-up
We are given a file with what appears to be a flag format but in really weird font. This reminded me of a childhood book I used to read about being a spy, so I search up [pigpen cipher](https://en.wikipedia.org/wiki/Pigpen_cipher). Seems like this is is not the actual pigpen cipher but a variant of it by the knights. So we set out to decrypt it.

Apparently, `CROSSCTF{LING_FOR_YOU}` is wrong, what's up with that?

Therefore, the flag is `CROSSCTF{KING_FOR_YOU}`.