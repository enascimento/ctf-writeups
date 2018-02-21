# EasyCTF_2018: Souper Large Primes

**Category:** Cryptography
**Points:**
**Description:**

>Technically I used strong primes. But are they really strong in this case? They are big, but there might still be an issue here. [n.txt](n.txt) [e.txt](e.txt) [c.txt](c.txt).

## Write-up
This challenge was relatively simple, except that it required a bit of tweaking to actually decrypt the mesage in time. Firstly, the values of `p` and `q` was easily factored with the help of Fermat's algorithm, particularly using the [attackrsa](https://github.com/rk700/attackrsa) tool.

    # attackrsa -t fermat -n $(cat n.txt)
    ====== Cracked! =======
    p is 0x42178a3d54[...]
    q is 0x42178a3d53[...]

After getting `p` and `q`, we can easily calculate `d` with `gmpy2` but instead of going that route, I chose to use [CRT](https://en.wikipedia.org/wiki/Chinese_remainder_theorem) to decrypt the message. Even with CRT, it took my Macbook a good 20-30 minutes to decrypt the message. Lame.

    # Use CRT to decrypt
    dp = gmpy2.invert(e, (p-1))
    dq = gmpy2.invert(e, (q-1))
    qinv = gmpy2.invert(q, p)

    # Get message
    m1 = gmpy2.powmod(c, dp, p)
    m2 = gmpy2.powmod(c, dq, q)
    h = (qinv * (m1 - m2)) % p 
    m = m2 + h * q

With that, quickly formulate a [Python](solve.py) script to crack our message for us.

    # ./solve.py 
    110010101100001011100110111100101100011011101000110011001111011010100110111010001110010001100000110111001100111010111110111000001110010011010010110110100110011011100110101111101101110001100000111010001011111011100110011000001011111011100110111010001110010001100000011000000110000011011100110011101111101

    # rax2 -b 110010101100001011100110111100101100011011101000110011001111011010100110111010001110010001100000110111001100111010111110111000001110010011010010110110100110011011100110101111101101110001100000111010001011111011100110011000001011111011100110111010001110010001100000011000000110000011011100110011101111101
    ???????????`?ξ????f??`??`????```??

Our `m` was this weird string of numbers, maybe it's binary? Well, decoding it from binary proved fruitless, let's add a `0` in front of it.
    
    # rax2 -b 011001010110000110011001111011010100110111010001110010001100000110111001100111010111110111000001110010011010010110110100110011011100110101111101101110001100000111010001011111011100110011000001011111011100110111010001110010001100000011000000110000011011100110011101111101
    easyctf{Str0ng_prim3s_n0t_s0_str000ng}

Therefore, the flag is `easyctf{Str0ng_prim3s_n0t_s0_str000ng}`.
