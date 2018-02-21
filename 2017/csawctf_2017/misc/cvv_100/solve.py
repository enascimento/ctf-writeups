#! /usr/bin/env python3
##
# Created for the CSAW CTF 2017
# By Amos (LFlare) Ng <amosng1@gmail.com>
##
# Imports
from pwn import *
import random
import re


def generate_card(prefix=None, suffix=None):
    card = "000000"

    while True:
        if prefix is not None:
            card = prefix

        # Check amount we should generate
        length = 9
        if suffix is not None:
            length -= (len(suffix) - 1)

        # Generate remaining numbers
        for i in range(length):
            card += str(random.randrange(9))

        # Append to numbers if suffix has more
        if suffix is not None:
            card += suffix[:-1]

        # Get sum of digits
        total = 0
        for i, num in enumerate(card[::-1]):
            num = int(num)

            # If odd digit, multiply by 2
            if i % 2 == 0:
                num = num * 2

                # If bigger than 9, sum digits
                if num > 9:
                    num = str(num)
                    num = int(num[0]) + int(num[1])

            # Add to total
            total += num

        # Calculate final checksum
        checksum = str((10 - (total % 10)) % 10)

        # Finalize card
        card += checksum

        # If requiremens matched
        if suffix is None or card.endswith(suffix):
            return card


def check_card(card):
    total = 0
    for i, num in enumerate((card[:-1])[::-1]):
        num = int(num)

        # If odd digit, multiply by 2
        if i % 2 == 0:
            num = num * 2

            # If bigger than 9, sum digits
            if num > 9:
                num = str(num)
                num = int(num[0]) + int(num[1])

        # Add to total
        total += num

    # Calculate final checksum
    checksum = str((10 - (total % 10)) % 10)

    # Return status
    return "1" if checksum == card[-1] else "0"

# Create tube
t = remote("misc.chal.csaw.io", "8308")

# Read cards
# context.log_level = "debug"
while True:
    response = t.recvline().decode()
    reply = None

    # Check type
    if "American" in response:
        reply = generate_card("37144")
    elif "Visa" in response:
        reply = generate_card("412345")
    elif "Master" in response:
        reply = generate_card("511234")
    elif "Discover" in response:
        reply = generate_card("651234")
    elif "starts with" in response:
        reply = generate_card(re.findall("[0-9]+", response)[0])
    elif "ends with" in response:
        reply = generate_card("123456", re.findall("[0-9]+", response)[0])
    elif "valid" in response:
        reply = check_card(re.findall("[0-9]+", response)[0])
    elif "flag" in response:
        log.success(response)
        quit()

    # Send reply
    if reply is not None:
        t.sendline(reply)
        log.info("Sending: " + reply)
