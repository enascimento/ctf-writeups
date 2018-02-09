# GryphonCTF_2016: Shark Web

**Category:** Web
**Points:** 10
**Description:**

>One of our admins was testing his secret web page in the organisation's internal network. A very skilled hacker listened to his packets.. Can you sniff his credentials from it..?
Play at http://play.spgame.site:9995
Creator - Chen Qiurong (@pc84560895)

## Write-up
This time around, we get a [PCAP file](dump.pcapng). We can use a tool like [WireShark](https://www.wireshark.org/). Opening the file and opening packet #4, you notice two fields `user` and `pass`. Could they be the credentials?

Entering the username `IwannaWatch` and password `SumMovies` into the page at `http://play.spgame.site:9995/`, you get a page with the flag.

Therefore, the flag is `GCTF{3ncryp7_y0ur_c0nn3c710n}`.
