# EasyCTF_2018: Netcat

**Category:** Intro
**Points:** 20
**Description:**

>I've got a little flag for you! Connect to c1.easyctf.com:12481 to get it, but you can't use your browser!
(Don't know how to connect? Look up TCP clients like Netcat. Hint: the Shell server has Netcat installed already!)
Here's your player key: 391834438. Several challenges might ask you for one, so you can get a unique flag!

## Write-up
Simple challenge, just use netcat, or `nc`.

    root@ctf:~# nc c1.easyctf.com 12481
    enter your player key: 391834438
    thanks! here's your key: easyctf{hello_there!_94A17F16678CeCA3}

Therefore, the flag is `easyctf{hello_there!_94A17F16678CeCA3}`.
