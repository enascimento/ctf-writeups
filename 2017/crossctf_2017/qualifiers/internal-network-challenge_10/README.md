# CrossCTF_2017: Internal Network Challenge

**Category:** Web
**Points:** 10
**Description:**

>We found out that winc0rp has an internal website hosted on this ip address. However, is it really internal?
I heard the internal website is located at 'internal.proxy.winc0rp.com' 
Please find the internal website hosted on 128.199.98.78:8080

## Write-up
VirtualHosts is a finnicky thing.

    $ curl "http://128.199.98.78:8080" -H "Host: internal.proxy.winc0rp.com"
    Flag is:
    CrossCTF{B@sic_P3ntesting_Sk33ls_Requir3d}

Therefore, the flag is `CrossCTF{B@sic_P3ntesting_Sk33ls_Requir3d}`.