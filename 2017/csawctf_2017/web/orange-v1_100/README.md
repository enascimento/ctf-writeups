# CSAWCTF_2017: Orange V1

**Category:** Web
**Points:** 100
**Description:**

>I wrote a little proxy program in NodeJS for my poems folder.
Everyone wants to read flag.txt but I like it too much to share.
http://web.chal.csaw.io:7311/?path=orange.txt

## Write-up
This is a challenge on directory transversal attacks, with the focus on encoding the payload such that attacking it requires a double-encoded payload.

Our original attempt at `http://web.chal.csaw.io:7311/?path=../` immediately responded with `WHOA THATS BANNED!!!!`. This led me to believing that `..` is banned. So, to bypass this, all we have to do is double encode the `.` to `%252e`. Navigating to `http://web.chal.csaw.io:7311/?path=%252e%252e/flag.txt` gives us the flag.

Therefore, the flag is `flag{thank_you_based_orange_for_this_ctf_challenge}`.
