# EasyCTF_2018: Pixelly

**Category:** Reverse
**Points:** 220
**Description:**

>I've created a new [ASCII art generator](http://c1.easyctf.com:12489/), and it works beautifully! But I'm worried that someone might have put a backdoor in it. Maybe you should check out the [source](asciinator.py) for me...

## Write-up
**_Disclaimer: Writeup for this challenge is poorly done due to my laziness, just refer to the script provided at the end. Sorry._**
This challenge was one of the most fun I've had, not that it was too easy or anything but essentially, the targetted line was,

    # hehehe
    try:
        eval(arr)
    except SyntaxError:
        pass

where `arr` was the image converted to ASCII art. Looking at the charset, we can formulate a plan to execute stuff that it should not.

    chars = np.asarray(list(' -"~rc()+=01exh%'))

After a bit of tweaking, the following seems like the best bet would be to call something like `exec(eval(flag))`. Since we have the charset for `exec`, we only need to work on using `chr()` to get our characters for the `valfg` characters.

Now apparently, the generated image payload won't give us the flag, this is simply because of the extra whitespace newlines that our empty image produces. To fix, simply generate an image that's `10` pixels or lower in height.

**_Disclaimer, for some reason, my script did not want to transcribe `-` characters properly, so I just converted everything to using `+`s._**

Finally, using our now [finalised script to generate our payload](solve.py), submit our [generated image](flagger.png) for submission. With that, we get our flag too.

Therefore, the flag is `easyctf{wish_thi5_fl@g_was_1n_ASCII_@rt_t0o!}`.
