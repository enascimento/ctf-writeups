# PACTF_2017:

**Category:**
**Points:** 40
**Description:**

>Those Dinosaurs… had money?
Turns out they also created a ledger system.

**Hint:**

>I wonder what entry you’re looking for…

## Write-up
Revisiting our old dinosaur site, we find an interesting tidbit.

    $ dig TXT ledger.dinosaurneverforgetsystem.tk

    ; <<>> DiG 9.8.3-P1 <<>> TXT ledger.dinosaurneverforgetsystem.tk
    ;; global options: +cmd
    ;; Got answer:
    ;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 58605
    ;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0

    ;; QUESTION SECTION:
    ;ledger.dinosaurneverforgetsystem.tk. IN    TXT

    ;; ANSWER SECTION:
    ledger.dinosaurneverforgetsystem.tk. 14141 IN TXT "3890a940bf54bb50d2ad334d0d0ddbda8a8737b6873277412756724292e89e31"

    ;; Query time: 7 msec
    ;; SERVER: 164.78.239.15#53(164.78.239.15)
    ;; WHEN: Tue Apr 18 13:58:43 2017
    ;; MSG SIZE  rcvd: 130

What does `3890a940bf54bb50d2ad334d0d0ddbda8a8737b6873277412756724292e89e31` mean? Decoding it into ASCII gives nothing, let's try to search it. [BAM!](https://blockchain.info/tx/3890a940bf54bb50d2ad334d0d0ddbda8a8737b6873277412756724292e89e31)

Therefore, the flag is `those_dinosaurs_sure_are_clever`.