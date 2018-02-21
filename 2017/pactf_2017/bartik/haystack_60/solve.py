#! /usr/bin/env python3
##
# Created for the Haystack challenge
# By Amos Ng
##
# Imports
import json
import base64
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

def verify_sign(pubkey, signature, data):
    verifier = PKCS1_v1_5.new(pubkey)
    shadigest = SHA256.new()
    shadigest.update(base64.b64decode(data))
    if verifier.verify(shadigest, base64.b64decode(signature)):
        return True
    return False

# Open file
data = json.loads(open("haystack.json", "r").read())

# Build pubkey
N = int(data["publicKey"]["modulus"])
E = int(data["publicKey"]["publicExponent"])
pubkey = RSA.construct((N, E)).publickey()

# Loop through data
for pair in data["haystack"]:
    # print("Looping!")
    data = pair["data"]
    signature = pair["signature"]

    if not verify_sign(pubkey, signature, data):
        print(base64.b64decode(data).decode())

