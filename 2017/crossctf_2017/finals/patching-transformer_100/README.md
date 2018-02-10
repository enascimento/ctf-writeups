# CrossCTF_2017: Patching transformer

**Category:** Defense
**Points:** 100
**Description:**

>Patch the broken transformer!
Use the following command
curl -v -F secretKey=@localFile 192.168.0.30:8080/api/transformer
[Binary to patch here](transformer_wm)

## Write-up
This is a really simple one and is easily defeated by nopping most parts of the binary. In this case, we can exploit this by buffer overflowing word 1 with `256` bytes of maximum bytes, followed by `4` bytes of `junk`, followed by `4` bytes of pointer pointing to `stealth()`.

To patch, all we have to do is to `NOP` either the `scanf` operation or even hex edit `stealth()` to immediately `leave` & `ret`. There's no fixed solution.
