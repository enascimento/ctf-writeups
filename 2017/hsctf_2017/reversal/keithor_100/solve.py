#! /usr/bin/env python3
##
# Created for the Keithor challenge
# By Amos Ng
##
from base64 import *
from hashlib import *

# Given files
b64hash = b'NGY3OTgwN2E3YzQ3ZjY5N2JkNWYwNmJlZWY5NTVjZmRmNGZkYWVmOGFkZThlZGY3MDc4NThmZTQyOTRkNzgwZDY5ZDRkNmE4OTdkODU5OGNlMzE0MmQyMDc2NDBjYTUxZDgyMTVkMGQ2YzY5Mzg3M2ZkMzJjMWY2ZTQ2ODc1MDAyN2I1ZGIzNGI3ZDljZTBhNzk3NTNlY2M3M2RhNjY0YTk5NTg4OWUwZDM2ZGI0YmZjNjhkZjlmYzhkYTNkMzY5YjI2NmU2MTdhNjE1OGQxNmNjYWQ0MTg5ZjBhM2RjYWU2MmQ5YjEwM2I1MGIwZDQzMzdjOTYxNjM0NzFiNDIzZmMyOGYzY2RhMjk0MTdiNzI4MGViOTMyMTQ5MjA3NWM1ODkwZGMwMzM0NzFjZjkxNzgxYTA3MDAxY2VhNjY5NmIzMmNkZjU2YjIxMjliYzc2YTgzMjE4YmVlNTJjODMwYThiZmMwOWVjNTVhZTM3MjExMGMwY2M4OTUwZWY1NzdkMzJlZDIxMWQ0MDMwN2MzZmQ2Njg0MTEzMzQxZTYwM2M='

# Calculate separate hashes
b16hash = b64decode(b64hash).decode()
md5hash = b16hash[0:32]
sha1hash = b16hash[32:72]
print("MD5 of Flag: %s" % md5hash)
print("SHA1 of Flag: %s" % sha1hash)

# Search up MD5 breaking tools online...
flag = b64encode(b"NVL7OA").decode()
assert flag == "TlZMN09B"

print("Flag: %s" % flag)