# PACTF_2017: Visual Words

**Category:**
**Points:** 70
**Description:**

>Some of us are visual learners. Some of us learn best from texts. I’ve found the perfect [combination!](test.png) It was a bit dark though, so I had to make it brighter by some factor.

**Hint:**

>Number, words, colors, data. It’s all really just numbers and math right?

## Write-up
This challenge involves reading each pixel by pixel to get the character representation of the colour code within each pixel to form a word. We have to take advantage of the Pillow library to solve this.

[Script](solve.py)

Therefore, the key is `flag_HidingSomeFunStuffInThisImage!!`.