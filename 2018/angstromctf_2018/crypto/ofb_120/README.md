# AngstromCTF_2018: ofb

**Category:**Crypto
**Points:** 120
**Description:**

>defund made a simple OFB cipher, if you can even call it that. Here's the [source](encrypt.py) and the [encrypted flag](flag.png.enc).

## Write-up
This challenge is also pretty straight forward but rather than the OFB we are trying to break, we are trying to break the linear congruent generator number generator used in `encrypt.py`. To do that, we will need three outputs from the linear congruent generator and we can do that by xorring the output of the first 12 bytes of the encrypted flag with the default standard PNG header pattern.

    x1 = int.from_bytes(data[:4], "big") ^ int.from_bytes(b"\x89\x50\x4e\x47", "big")
    x2 = int.from_bytes(data[4:8], "big") ^ int.from_bytes(b"\x0d\x0a\x1a\x0a", "big")
    x3 = int.from_bytes(data[8:12], "big") ^ int.from_bytes(b"\x00\x00\x00\x0d", "big")

After that is done, we can just use some nifty math to reverse our LCG's settings, `a` and `c`. Building a [script](solve.py) will allow us to automate this better.

    # ./solve.py 
    x1:  2445943554
    x2:  2225636917
    x3:  1320590709
    a:  3204287424
    c:  1460809397
    === VERIFY ===
    x1:  2445943554
    x2:  2225636917
    x3:  1320590709

With that, we get our flag,

![flag](flag.png)

Therefore, our flag is `actf{pad_rng}`.
