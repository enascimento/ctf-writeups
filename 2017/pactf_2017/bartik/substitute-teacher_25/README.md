# PACTF_2017: Substitute Teacher

**Category:**
**Points:** 25
**Description:**

>Mr. Michael S. “Mike” Rogers is the substitute teacher for the day, but he is having trouble deciphering the secret message that was left for him by the teacher. Mr. Rogers knows the note is in English, but that’s about all. Can you help him? [ENCRYPTED.txt](encrypted.txt)

**Hint:**

>Frequency analysis.

## Write-up
We go to [quipqiup] for this.

Using clues like,

    adim=flag
    cdixqkruk=plaintext

We get the plaintext,

    In cryptography, a substitution cipher is a method of encoding by which units of plaintext are replaced with ciphertext, according to a fixed system; the "units" may be single letters (the most common), pairs of letters, triplets of letters, mixtures of the above, and so forth. The receiver deciphers the text by performing the inverse substitution. (Wikipedia.org, "Substitution cypher") This is, for your sake, a completely normal English text. We were so nice, we decided to leave capitalization in the encrypted text... & punctuation! Aren't we nice. There is a relatively normal letter distribution in this text, so it shouldn't have been too difficult to solve. Anyway, congratulations! Here is your flag: only_slightly_better_than_caesar

Therefore, the flag is `only_slightly_better_than_caesar`.