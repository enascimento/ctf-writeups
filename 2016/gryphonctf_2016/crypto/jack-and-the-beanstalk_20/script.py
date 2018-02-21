#! /usr/bin/env python
##
import re
import random
import socket
import sys

successes = 0
seeded = False
first_no = 0

def get_answer(f, i):
    r = random.Random()
    r.seed(f)
    answer = 0
    for i in range(i):
        answer = r.randint(1, 100)
    return answer

while True:
    s = socket.socket()
    s.connect(('play.spgame.site', 9999))
    iters = 1

    while True:
        r = random.Random()
        data = s.recv(4096)

        if data != "":
            print("RECV>>>" + data.strip())

            if "GCTF" in data:
                sys.exit(0)

            if "Well done!" in data:
                successes += 1
                iters += 2
            if "number is" in data:
                try:
                    number = int(re.findall('[0-9]+', data)[1])
                except IndexError:
                    number = int(re.findall('[0-9]+', data)[0])

                if not seeded:
                    first_no = number
                    seeded = not seeded

                reply = get_answer(first_no, iters)
                print('Replied with number %d from seed %d' % (reply, first_no))
                s.send(str(reply) + "\n")
                continue