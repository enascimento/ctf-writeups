# EasyCTF_2018: In Plain Sight

**Category:** Web
**Points:** 70
**Description:**

>I've hidden a flag somewhere at [this](http://blockingthesky.com/) site... can you find it?

## Write-up
Easily solved with the help of DNS.

    $ dig TXT blockingthesky.com

    ; <<>> DiG 9.8.3-P1 <<>> TXT blockingthesky.com
    ;; global options: +cmd
    ;; Got answer:
    ;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 3137
    ;; flags: qr rd ra; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 0

    ;; QUESTION SECTION:
    ;blockingthesky.com.        IN  TXT

    ;; ANSWER SECTION:
    blockingthesky.com. 29  IN  TXT "_globalsign-domain-verification=kXlECiyonFE_qsQR-8ki6BOIdVru3bzxpwMDZr334_"
    blockingthesky.com. 29  IN  TXT "easyctf{betcha_wish_you_could_have_used_ANY}"

    ;; Query time: 88 msec
    ;; SERVER: 192.168.144.1#53(192.168.144.1)
    ;; WHEN: Sun Feb 11 15:49:37 2018
    ;; MSG SIZE  rcvd: 180

Therefore, the flag is `easyctf{betcha_wish_you_could_have_used_ANY}`.
