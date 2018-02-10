# PACTF_2017: Open Sourcery 2

**Category:**
**Points:** 40
**Description:**

>There are many strings in the source code of the latest Google Chrome. Some of the strings contain pactf. Find the one that starts with i, ends with e, and also contains the letter v.

**Hint:**

>Maybe you could get the source from the binary. But what’s this relationship between Chrome and Chromium I heard? Also, just so you know, this flag doesn’t have the string flag in or around it.

## Write-up
Just some tough [Googling](https://cs.chromium.org/chromium/src/net/http/transport_security_state_static.json?q=i.*pactf.*e&maxsize=4239506&l=24486).

Therefore, the flag is `impactfestival.be`.