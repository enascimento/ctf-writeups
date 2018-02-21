# EasyCTF_2018: EzSteg

**Category:** Forensics
**Points:** 30
**Description:**

>There appears to be a message beyond what you can see in [soupculents.jpg](soupculents.jpg).

## Write-up
This one was another easy challenge involving the use of `strings`.

    root@2895f837fc1c:~# strings soupculents.jpg 
    [...]
    ;48yY
    T8RT
    (aCt
    q$`I
    eE^]
    easyctf{l00k_at_fil3_sigS}

Therefore, the flag is `easyctf{l00k_at_fil3_sigS}`.
