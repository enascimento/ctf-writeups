#! /usr/bin/env python3
##
# Created for the Salted Hash Challenge
# By Amos Ng
##
from pwn import *
import binascii
import hashpumpy
import requests

# Variables given
site = "http://128.199.98.78:32769/index.php"
session = "user=john|pass=70e0f6cba9351375d1ec3440c6e2a5e41389d92c632baa1a28ca3d930c4a5a05|admin=0"
session_hash = "7e2967c611fc7e66b2e75a2fcb4ef80cdc75c91c8967ef058203d99688a146ab"
new_footer = "|admin=1"

# Loop through unknown key length
for i in range(60, 65):
    # Create messages
    digest, message = hashpumpy.hashpump(session_hash, session, new_footer, i)
    message = binascii.hexlify(message).decode()

    # Prepare cookies
    cookies = {"session": message,
               "session_hash": digest}

    r = requests.get(site, cookies=cookies)
    if "not admin" not in r.text:
        print(r.text)
