#! /usr/bin/env python3
##
# Created for EasyCTF 2018_
# By Amos (LFlare) Ng <amosng1@gmail.com>
##
from pwn import *
from zipfile import ZipFile
import re

# Import CSV
locations = dict()
with ZipFile("zcta.csv.zip") as zipfile:
    with zipfile.open("zcta.csv") as file:
        data = file.read().decode()
        for line in data.split("\n"):
            fields = line.split("\t")
            try:
                zipcode = fields[0].strip()
                land = fields[3].strip()
                water = fields[4].strip()
                lat = fields[7].strip()
                lng = fields[8].strip()

                locations[zipcode] = (lat, lng, land, water)
            except:
                pass

# Fun messages
# context.log_level = "debug"

# Open our pipes
t = remote("c1.easyctf.com", 12483)
t.recvuntil("====+")
rounds = 0
with log.progress("Cracking ECDSA...") as p:
    while True:
        # Log
        p.status(f"Round {rounds+1}")

        # Check if we already reached the end
        if rounds == 50:
            # Log flag
            p.success("Cracked!")
            log.success(t.recvuntil("}").decode())
            t.close()
            break
        else:
            # Dump output
            t.recvuntil("/ 50\n")

            # Get question
            question = t.recvuntil("? ").decode()

        # Parse zipcode
        zipcode = re.findall("([0-9]+)(?:\?)", question)[0]

        # Check questions
        rounds += 1
        if "latitude" in question:
            t.sendline(locations[zipcode][0])
        elif "longitude" in question:
            t.sendline(locations[zipcode][1])
        elif "land" in question:
            t.sendline(locations[zipcode][2])
        elif "water" in question:
            t.sendline(locations[zipcode][3])

        # Get rid of happiness
        t.recvuntil("correct!\n\n")
