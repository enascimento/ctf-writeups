# PACTF_2017: Authorization Of Time

**Category:**
**Points:** 55
**Description:**

>[qr.png](qr.png). 1489798809000. Get me in.

**Hint:**

>Big ben just hit 1.

## Write-up
We are originally given the Unix timestamp `1489798809000`, which translates to `11/05/49179 @ 6:30pm (UTC)`. Impossible, let's take this as a millisecond timestamp and remove 3 `0`s, bringing us to `1489798809`, which then translates to `03/18/2017 @ 1:00am (UTC)`. This makes much more sense.

In the QR code, we find out that the QR code contains an encoded `Time-based One-time Password Algorithm` or `TOTP` secret. Making use of the `pyotp` library, I made a nice [script](solve.py).

Therefore, the flag is `808365`.