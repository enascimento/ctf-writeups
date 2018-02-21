#! /usr/bin/env python
## Written by zst123
import socket
import re

s = socket.socket()
s.connect(('play.spgame.site', 8000))

while True:
    data = s.recv(4096)
    if data != "":
        print("RECV>" + data)
        if "Nearest pokemon" in data:
            coordinates = re.findall('\w=([-]?[0-9]+)', data)
            pokemonX = int(coordinates[0])
            pokemonY = int(coordinates[1])
            currentX = int(coordinates[2])
            currentY = int(coordinates[3])

            if currentX > pokemonX:
                currentX -= 1
            elif currentX < pokemonX:
                currentX += 1
            if currentY > pokemonY:
                currentY -= 1
            elif currentY < pokemonY:
                currentY += 1

            response = 'spoof %d,%d' % (currentX, currentY)
            s.send(response)
        elif "appears!" in data:
            response = 'catch'
            s.send(response)
        elif "Congratulations":
            break