# AngstromCTF_2018:

**Category:** Web
**Points:** 30
**Description:**

>Get me! Over [here](http://web.angstromctf.com:3005/).

## Write-up
We are brought to a page with a single submit button that leads us to the url `http://web.angstromctf.com:3005/?auth=false`. Notice how there is a `auth=false`, thus let's try `http://web.angstromctf.com:3005/?auth=true`.

    Here you go: actf{why_did_you_get_me}

Therefore the flag is `actf{why_did_you_get_me}`.
