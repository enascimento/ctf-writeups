# CrossCTF_2017: Patching Secrit Donut Tuch

**Category:** Defense
**Points:** 150
**Description:**

>Patch the secrit-binary-dunut-tuch!
Use the following command
curl -v -F secretKey=@localFile 192.168.0.30:8080/api/secrit_binary_donut_tuch
[Binary to patch here](secrit_binary_donut_tuch_wm)

## Write-up
This one is an extension of [Patching transformer](../patching-transformer_100) as it can be solved in a similar way. The key idea is simple, to convert all the `JNE` symbols to `JMP` symbols to skip the section of code that will print the flag.

![Screenshot 1](screenshot-1.png)

![Screenshot 1](screenshot-2.png)

[Solution](secrit_binary_donut_tuch_wm_patched).
