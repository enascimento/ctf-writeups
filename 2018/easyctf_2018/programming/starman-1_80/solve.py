#! /usr/bin/env python3
##
# Created for EasyCTF 2018_Starman 1
# By Amos (LFlare) Ng <amosng1@gmail.com>
##
N, W = input().split(" ")
N = int(N)
W = int(W)

# Dark Magick
def knapsack(hackers, max_weight):
    k = [[0 for x in range(max_weight + 1)] for x in range(len(hackers) + 1)]

    # Loop through W^2
    for y, (hacker, weights) in enumerate(zip(hackers, k), 1):
        for x, current_weight in enumerate(weights[1:], 1):
            if hacker[1] <= x:
                k[y][x] = max(
                    hacker[0] + weights[x - hacker[1]],
                    current_weight)
            else:
                k[y][x] = current_weight

    return k[-1][-1]

# Get hackers
hackers = []
for i in range(N):
    # Read damn hackers
    n, w = input().split(" ")
    n = int(n)
    w = int(w)
    v = n / w

    # Add to array
    hackers.append((n, w))

# Print
print(knapsack(hackers, W))
