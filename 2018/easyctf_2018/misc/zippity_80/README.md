# EasyCTF_2018: Zippity

**Category:** Misc
**Points:** 80
**Description:**

>I heard you liked zip codes! Connect via `nc c1.easyctf.com 12483` to prove your zip code knowledge.

## Write-up
This challenge was tricky in that you had to know where to look for the census data. Upon connecting, you get some hints on where to look.

    # nc c1.easyctf.com 12483
    +======================================================================+
    | Welcome to Zippy! We love US zip codes, so we'll be asking you some  |
    | simple facts about them, based on the 2010 Census. Only the          |
    | brightest zip-code fanatics among you will be able to succeed!       |
    | You'll have 30 seconds to answer 50 questions correctly.             |
    +======================================================================+

    3... 2... 1...  Go!

    Round  1 / 50
      What is the water area (m^2) of the zip code 93550? 

Essentially, we have to look for 2010 census data. After poking around for quite some time, we get this [link](http://www2.census.gov/geo/docs/maps-data/data/gazetteer/Gaz_zcta_national.zip) on this [page](https://www.census.gov/geo/maps-data/data/gazetteer2010.html). Downloading the [archive](zcta.csv.zip) allows us to complete this challenge by [pure Python magick](solve.py).

    # ./solve.py 
    [+] Opening connection to c1.easyctf.com on port 12483: Done
    [+] Cracking ECDSA...: Cracked!
    [+] You succeeded! Here's the flag:
        easyctf{hope_you_liked_parsing_tsvs!}
    [*] Closed connection to c1.easyctf.com port 12483

Therefore, the flag is `easyctf{hope_you_liked_parsing_tsvs!}`.
