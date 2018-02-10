# CrossCTF_2017: Paricle Collision Challenge

**Category:** Cryptography
**Points:** 5
**Description:**

>Our large hadron collider feeds off files that produces the same SHA1 hashsum value. Could you help us power up our collider? We will give you a flag in return! Our collider can be found at http://128.199.98.78:8081/

**Hint:**

>The collider feeds on distinct pairs of files that produces the same SHA1 hashsum value.
However, the collider only accepts files it hasn't seen before!

## Write-up
This is a simple one, given that SHA1 is entirely broken and collisions are easily generated. For the purpose of this challenge, we will use a [SHA1 collider](http://alf.nu/SHA1), yielding two [PDFs that result in the same hash](sha.zip).

Therefore, the flag is `CrossCTF{P@rticl3_C0llid3d!}`.