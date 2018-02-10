# CrossCTF_2017: complexpassword

**Category:** Misc
**Points:** 5
**Description:**

>We found out that evilc0rp has a password policy stating that passwords should:
- Contain upper case characters
- Contain lower case characters
- Contain digits
- Contain nonalphanumeric characters: (~!@#$%^&*_-+=`|\(){}[]:;"'<>,.?/)
However, it'd take too long to try every possible password in the password list we found.
Can you help us develop a regex to find the correct passwords more efficiently?
p.s. We need 6 of them and I think they use really strong passwords...
Password list [here](10m_list)
Connect to 128.199.98.78:32768

## Write-up
Just some nifty lookahead regex configuration and we have the flag.

    $ nc 128.199.98.78 32768
    We found out that evilc0rp has a password policy stating that passwords should:
    - Contain upper case characters
    - Contain lower case characters
    - Contain digits
    - Contain nonalphanumeric characters: (~!@#$%^&*_-+=`|\(){}[]:;"'<>,.?/)

    However, it'd take too long to try every possible password in the password list we found.
    Can you help us develop a regex to find the correct passwords more efficiently?
    p.s. We need 6 of them and I think they use really strong passwords...

    Regex: ^(?=.*[a-z])(?=.*[A-Z])(?=.*[~!@#$%^&*_\-+=`|(){}[\]:;"'<>,.?/])(?=.*[0-9]).{25,}$

    Filtering passwords!...
    1) Vixens.comreaper999MOR098GO
    2) Tickled.comreaper999MOR098GO
    3) Your_Guardian_Angel_050813
    4) you_have_been_hacked_gWSxH1FZfr
    5) weAaQIno0lhLHWsIfL9TQG30ZrI-~B
    6) &&wdXWabuSc7&b*QDex_6B*5v?e8V
    Congratulations! Here's your flag: CrossCTF{C0mPleX_P@s$w0rd_Is_G0oD!}

Therefore, the flag is `CrossCTF{C0mPleX_P@s$w0rd_Is_G0oD!}`.