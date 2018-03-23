# AngstromCTF_2018: md5

**Category:** Web
**Points:** 140
**Description:**

>defund's a true MD5 fan, and he has a [site](http://web.angstromctf.com:3003) to prove it.

## Write-up
This is one of defund's worser challenges ever. Essentially, he disguised a web challenge as a crypto challenge and I wasted too much time researching on unknown prefix collision attacks.

Essentially, this challenge can be boiled down to arrays. By submitting both variables as arrays, we are able to bypass the `===` identicallity check while also having the same value. This is because when an array is concated onto a string, it merely becomes `Array`.

By accessing `http://web.angstromctf.com:3003/?str1[]=0&str2[]=1`, we get the flag.

Therefore, the flag is `actf{but_md5_has_charm}`.
