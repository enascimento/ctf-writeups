# EasyCTF_2018: Reverse Engineering

**Category:** Intro
**Points:** 30
**Description:**

>What does this [Python program](https://easyctf.com/chals/autogen/89/mystery.py) do? And more specifically, what input would give this output?
6538c2937cc3bb20c3983ac2ab4901c38fc297161fc2a6c3b3c281c28107c2a7c2a03fc3956ec3b55350

## Write-up
This one was a simple one as well, just with a twist of `UTF-8`. Solving this is just knowing that XOR operations are entirely reversable and therefore, we just have to input our output back in to get our input.

    cipher = b"6538c2937cc3bb20c3983ac2ab4901c38fc297161fc2a6c3b3c281c28107c2a7c2a03fc3956ec3b55350"
    def unmystery(s):
        r = ""
        for i, c in enumerate(s):
            r += chr(ord(c) ^ ((i * ord(key[i % len(key)])) % 256))
        return r

    print(unmystery(binascii.unhexlify(cipher).decode("utf-8")))

The full script is available [here](mystery.py).

    root@ctf:~/downloads# ./mystery.py 
    easyctf{char_by_char_41d6D3}

Therefore, the flag is `easyctf{char_by_char_41d6D3}`.
