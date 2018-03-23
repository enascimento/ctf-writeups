# AngstromCTF_2018: slots

**Category:** Misc
**Points:** 90
**Description:**

>defund is building a casino empire. Break his [slot machine](slots.py), which is running at `web.angstromctf.com:3002`. Note: connect with netcat or an equivalent tool.

## Write-up
This challenge is a mere teaser on one of Python's quirks with integers, that it could be `NaN` or not a number. If it is not a number, it simply cannot be used to check if it's below `0`, above `money` or `1000000000`. As such, we can break this challenge with just one bet.

    $ nc web.angstromctf.com 3002
    Welcome to Fruit Slots!
    We've given you $10.00 on the house.
    Once you're a high roller, we'll give you a flag.
    You have $10.00.
    Enter your bet: NaN
    🍐 : 🍈 : 🍈
    🍉 : 🍇 : 🍒 ◀
    🍒 : 🍌 : 🍒
    You lost everything.
    Wow, you're a high roller!
    A flag: actf{fruity}

Therefore, the flag is `actf{fruity}`.
