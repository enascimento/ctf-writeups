# EasyCTF_2018: RSA_v

**Category:** Cryptography
**Points:** 200
**Description:**

>Bob is extremely paranoid, so he decided that just one RSA encryption is not enough. Before sending his message to Alice, he forced her to create 5 public keys so he could encrypt his message 5 times! Show him that he still is not secure... [rsa.txt](rsa.txt).

## Write-up
This challenge revolves around the underlying principle of RSA and how encrypting a message 5 times with increasing exponents ultimately leads to complete confidentiality exploitation. The very base of the formula goes along something like this,

    c = m^e mod n

However, by encrypthing it multiple times with the same `n` but differing `e` you get,

    c1 = m^e1 mod n
    c2 = c1^e2 mod n
    c3 = c2^e3 mod n
    c4 = c3^e4 mod n
    c5 = c4^e5 mod n

Which when compiled looks like

    c5 = ((((m^e1)^e2)^e3)^e4)^e5 mod n

As powers simply multiply up, where `2^(3^2)` is just `2^6`, we can calculate the effective `e`.

    e = e1 * e2 * e3 * e4 * e5
      = 27587468384672288862881213094354358587433516035212531881921186101712498639965289973292625430363076074737388345935775494312333025500409503290686394032069

Now that we have the effective `e` we can produce our proper challenge,

    e = 27587468384672288862881213094354358587433516035212531881921186101712498639965289973292625430363076074737388345935775494312333025500409503290686394032069
    n = 9247606623523847772698953161616455664821867183571218056970099751301682205123115716089486799837447397925308887976775994817175994945760278197527909621793469
    c = 7117565509436551004326380884878672285722722211683863300406979545670706419248965442464045826652880670654603049188012705474321735863639519103720255725251120

`e` seems like a really big number, similar to smallRSA of PicoCTF, let's try the [same exploit, using Wiener's Attack](https://en.wikipedia.org/wiki/Wiener%27s_attack), as we used back then! Literally ripped almost the [same script from back then](solve.py).

    # ./solve.py 
    easyctf{keblftftzibatdsqmqotemmty}

Therefore, the flag is `easyctf{keblftftzibatdsqmqotemmty}`.
