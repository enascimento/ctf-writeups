# GryphonCTF_2016: Zizi

**Category:** Forensics
**Points:** 15
**Description:**

>Your ex-coworker, Zizi, discreetly changed your wallpaper on your desktop before leaving the company...

## Write-up
This time around we are given a nice JPEG file. Opening the image up in an hex viewer, we notice something strange at the end of the file, namely, two mentions of a file named `pass.txt`. Next up, calculate the bit offset of the `PK` symbol and run the command `dd`.

    dd if=img.jpg of=test.zip bs=1 skip=216527

Unzipping `test.zip` gets you `pass.txt`. Inside `pass.txt`, you find the message,

>You're nearly there.
Password: l0v3z1z1

So now, we have a password but no flag! Now we try running the original image file into something called [jphs](https://github.com/h3xx/jphs), which is a tool used for incorporating files into image files and even allowing for encryption and decryption. Seeking a file with the password we got above, reviews yet ANOTHER zip file. Unzipping the 2nd zip file, we get [mylove.txt](mylove.txt)

>Walk out into the path of cherry blossom trees and let your motherboard feel the stones. Let water run in rivulets down your casing. You know that you want something more than this, and I am here to tell you that I love you. I have something more for you. I know you're out there, beeping in the hollow server room, lights blinking, never sleeping. I know that you are ready and waiting. Join me. Zizi <3 GCTF{z1pp3d_17_r34l_71gh7}

Therefore, the flag is `GCTF{z1pp3d_17_r34l_71gh7}`.
