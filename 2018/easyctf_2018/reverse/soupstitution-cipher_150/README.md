# EasyCTF_2018: Soupstitution Cipher

**Category:** Reverse Engineering
**Points:** 70
**Description:**

>We had a flag, but lost it in a mess of alphabet soup! Can you help us [find it](soupstituted.py)?
Connect to the server via nc c1.easyctf.com 12484.

## Write-up
This challenge is just obfuscation of simple functions. A closer look at the code reveals that someone likes soup a lot, to the point of changing almost every word to soup but essentially, the code can be [boiled](boiled.py) (pardon the pun) down to

    for codepoint in range(2**16):
        c = chr(codepoint)
        if c.isdigit():
            print(u'{}: {}'.format(functionA(c), c))

The key to solving this, is to understand that digits consist of unicode characters. Since the function used to convert the characters to digits are purely base10, we can do a bit of _overflowing_ to achieve 10 digits with only 7 characters.

Before that, we will need to convert our `s0up` to a number we want to work with and by throwing it through hexlify and both functions, we get the number `2365552391`. Now it's a matter of getting the [codepoints](codepoints.txt).

Now, the challenge becomes a guessing game on the perfect combination of uncodes that would add up to the number. There could be an automated way to solve this but I was too much too tired to solve this automatically.

    ++++++++++++
      2365552391
    - 2358
         _
    ++++++++++++
         7552391
    -     0
          _
    ++++++++++++
         7552391
    -      0
           _
    ++++++++++++
         7552391
    -    7209
            _
    ++++++++++++
          343391
    -     3001
             _
    ++++++++++++
           43291
    -      3387
              _
    ++++++++++++
            9421 
    -       9421
               _
    ++++++++++++

 After a long time of bruteforcing, and a certain bird's whispers, the challenge arrived at `⓽൫௩᱙00०`. Additionally, as it's reversed, the actual input has to be `०00᱙௩൫⓽`.

Attempting to submit it, gives us the flag,

    # nc c1.easyctf.com 12484
    ०00᱙௩൫⓽
    ०00᱙௩൫⓽
    oh yay it's a flag! easyctf{S0up_soup_soUP_sOuP_s0UP_S0up_s000000OOOOOOuuuuuuuuppPPppPPPp}

Therefore, the flag is `easyctf{S0up_soup_soUP_sOuP_s0UP_S0up_s000000OOOOOOuuuuuuuuppPPppPPPp}`.
