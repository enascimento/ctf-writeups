# EasyCTF_2018: Web

**Category:** Intro
**Points:** 10
**Description:**

>The web goes well beyond the surface of the browser! Warm up your web-sleuthing skills with this challenge by finding the hidden flag on this [page](https://cdn.easyctf.com/048c63edc2ffec871a3e3a8dce341e9f5c1493372734a429a5603ad0853f73c6_index.html)!

## Write-up
Another simple introductory challenge,

    root@ctf:~# curl https://cdn.easyctf.com/048c63edc2ffec871a3e3a8dce341e9f5c1493372734a429a5603ad0853f73c6_index.html

    <!doctype html>
    <html>
        <head>
            <style>
                body { font-family: sans-serif; padding-left: 30px; padding-top: 15px; }
            </style>
        </head>
        <body>
            <h1>Welcome to EasyCTF!</h1>

            <p>The flag is just below:</p>
            <!-- easyctf{hidden_from_the_masses_2978fa} -->
        </body>
    </html>

Therefore, the flag is `easyctf{hidden_from_the_masses_2978fa}`.
