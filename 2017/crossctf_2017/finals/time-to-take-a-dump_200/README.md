# CrossCTF_2017: Time To Take A Dump

**Category:** Hardware
**Points:** 200
**Description:**

>There seems to be something running on the FREE arduino! I wonder if I can talk to it...

## Write-up
I'll start off by saying I have 0 experience with hardware and am a complete noob. However, I have Google. Firstly, we need to accomplish dumping the flash memory of the Arduino Mega, accomplishable through `avrdude`.

Afterwards, we need to convert it to hexadecimal format for easier reading through using `avr-objdump`. From there, we can see a few interesting strings, like a very sneaky fake flag, a string that suspiciously looks like an encoding table and the original encoded string. After a little bit of twiddling, it does seem like a `base64` encoded string but not in the same form as the `base64` we all know and love.

So, this is a case of custom `base64`. Using a [site](https://www.malwaretracker.com/decoder_base64.php) recommended over at [zst123's GitHub](https://github.com/zst123/crossctf_finals-2017-writeups), we can decode the flag to `CrossCTF{Bas364_1z_hard}`.

Therefore, the flag is `CrossCTF{Bas364_1z_hard}`.
