#! /usr/bin/env python3
##
# Created for the GovTech Web Challenge Level 1
# By Amos <LFlare> Ng
##
# Define encoded flag
encoded_flag = "BCBCBADABCABBABDBDCDBDBABCBBBCAD" \
               "BCCABBDDBAACBCABBDADBCBBADBABDDB"

# Convert to integer representation in string
encoded_flag = "".join(str(ord(c) - 0x41) for c in encoded_flag)

# Convert to chunks of 4 characters
encoded_flag = [encoded_flag[i:i+4] for i in range(0, len(encoded_flag), 4)]

# Convert chunks to character representation in base 256
decoded_flag = []
for chunk in encoded_flag:
    chunk = chunk[::-1]
    total = int(chunk[0]) * (4 ** 0) + \
            int(chunk[1]) * (4 ** 1) + \
            int(chunk[2]) * (4 ** 2) + \
            int(chunk[3]) * (4 ** 3)
    decoded_flag.append(chr(total))

# Print result
print("Flag: %s" % "".join(decoded_flag))
