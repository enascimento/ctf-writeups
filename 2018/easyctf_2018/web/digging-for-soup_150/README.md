# EasyCTF_2018: Digging For Soup

**Category:** Web
**Points:** 150
**Description:**

>Perhaps this time I'll have hidden things a little better... you won't find my flag so easily now! [nicebowlofsoup.com](nicebowlofsoup.com)

## Write-up
A stupid challenge worth way too much. Initially, you find out that your usual TXT don't work,

    $ dig TXT nicebowlofsoup.com

    ; <<>> DiG 9.8.3-P1 <<>> TXT nicebowlofsoup.com
    ;; global options: +cmd
    ;; Got answer:
    ;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 36765
    ;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0

    ;; QUESTION SECTION:
    ;nicebowlofsoup.com.        IN  TXT

    ;; ANSWER SECTION:
    nicebowlofsoup.com. 80  IN  TXT "Close, but no cigar... where else could it be?"

    ;; Query time: 35 msec
    ;; SERVER: 192.168.144.1#53(192.168.144.1)
    ;; WHEN: Mon Feb 12 03:37:36 2018
    ;; MSG SIZE  rcvd: 95

A little bit of poking around later, you arrive at the stupidest solution of all,

    $ dig TXT easyctf.nicebowlofsoup.com

    ; <<>> DiG 9.8.3-P1 <<>> TXT easyctf.nicebowlofsoup.com
    ;; global options: +cmd
    ;; Got answer:
    ;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 46658
    ;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0

    ;; QUESTION SECTION:
    ;easyctf.nicebowlofsoup.com.    IN  TXT

    ;; ANSWER SECTION:
    easyctf.nicebowlofsoup.com. 299 IN  TXT "easyctf{why_do_i_even_have_this_domain}"

    ;; Query time: 59 msec
    ;; SERVER: 192.168.144.1#53(192.168.144.1)
    ;; WHEN: Mon Feb 12 03:34:45 2018
    ;; MSG SIZE  rcvd: 96

**_NINJA EDIT:_** After the challenge has been reworked, the solution requires the use of AXFR instead.

    $ dig ns2.nicebowlofsoup.com

    ; <<>> DiG 9.10.3-P4-Ubuntu <<>> ns2.nicebowlofsoup.com
    ;; global options: +cmd
    ;; Got answer:
    ;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 5587
    ;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

    ;; OPT PSEUDOSECTION:
    ; EDNS: version: 0, flags:; udp: 4096
    ;; QUESTION SECTION:
    ;ns2.nicebowlofsoup.com.        IN  A

    ;; ANSWER SECTION:
    ns2.nicebowlofsoup.com. 86145   IN  A   159.65.43.62

    ;; Query time: 1 msec
    ;; SERVER: 67.207.67.2#53(67.207.67.2)
    ;; WHEN: Tue Feb 20 14:56:55 UTC 2018
    ;; MSG SIZE  rcvd: 67

    $ dig axfr nicebowlofsoup.com @159.65.43.62

    ; <<>> DiG 9.10.3-P4-Ubuntu <<>> axfr nicebowlofsoup.com @159.65.43.62
    ;; global options: +cmd
    nicebowlofsoup.com. 86400   IN  SOA ns1.nicebowlofsoup.com. hostmaster.nicebowlofsoup.com. 2018021205 28800 7200 604800 86400
    easyctf.nicebowlofsoup.com. 10  IN  TXT "easyctf{why_do_i_even_have_this_domain}"
    nicebowlofsoup.com. 100 IN  TXT "Close, but no cigar... where else could it be? hint: the nameserver's IP is 159.65.43.62"
    nicebowlofsoup.com. 86400   IN  SOA ns1.nicebowlofsoup.com. hostmaster.nicebowlofsoup.com. 2018021205 28800 7200 604800 86400
    ;; Query time: 17 msec
    ;; SERVER: 159.65.43.62#53(159.65.43.62)
    ;; WHEN: Tue Feb 20 14:56:35 UTC 2018
    ;; XFR size: 4 records (messages 3, bytes 404)

Therefore, the flag is `easyctf{why_do_i_even_have_this_domain}`.
