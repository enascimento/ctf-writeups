# EasyCTF_2018: NoSource, Jr.

**Category:** Web
**Points:** 80
**Description:**

>I don't like it when people try to view source on my page. Especially when I put all this effort to put my flag verbatim into the source code, but then people just look at the source to find the flag! How annoying.
This time, when I write my wonderful website, I'll have to hide my beautiful flag to prevent you CTFers from stealing it, dagnabbit. We'll see what you're [able to find](http://c1.easyctf.com:12486/jr/)...

## Write-up
We are given a link to the site with 3 key ingredients. Firstly, the key,

    window.encryptionKey = 'nosource';

Then, the flag,

    var flag = 'Fg4GCRoHCQ4TFh0IBxENAE4qEgwHMBsfDiwJRQImHV8GQAwBDEYvV11BCA==';

Lastly, the function,

    function process(a, b) {
        'use strict';
        var len = Math.max(a.length, b.length);
        var out = [];
        for (var i = 0, ca, cb; i < len; i++) {
          ca = a.charCodeAt(i % a.length);
          cb = b.charCodeAt(i % b.length);
          out.push(ca ^ cb);
        }
        return String.fromCharCode.apply(null, out);
    }

However, the key is not the key! Let's get the key in Python instead,

    flag = base64.b64decode("Fg4GCRoHCQ4TFh0IBxENAE4qEgwHMBsfDiwJRQImHV8GQAwBDEYvV11BCA==")
    plaintext = "easyctf"
    for a, b in zip(flag, plaintext):
        print(chr(a ^ ord(b)))

We get this weird output,

    s
    o
    u
    p
    y
    s

Could it be `soupy`? Let's try it in our JS console again,

    > process(atob(flag), encryptionKey)
    "easyctf{congrats!_but_now_f0r_n0s0urc3_...}"

Therefore, the flag is `easyctf{congrats!_but_now_f0r_n0s0urc3_...}`.
