# EasyCTF_2018: Haystack

**Category:** Forensics
**Points:** 30
**Description:**

>There's a flag hidden in this [haystack](haystack.txt).

## Write-up
This challenge is just a little slightly obnoxious for older computers but using a little `grep` magic, you can pull the flag from thin air!

    root@ctf:~# cat haystack.txt | grep -Eo easyctf{.*}
    easyctf{tiXAuDCgmfDyMwNelDbPbWeyA}

Therefore, the flag is `easyctf{tiXAuDCgmfDyMwNelDbPbWeyA}`
