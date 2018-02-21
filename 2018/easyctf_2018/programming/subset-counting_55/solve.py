#! /usr/bin/env python3
##
# Created for EasyCTF 2018_Subset Counting
# By Amos (LFlare) Ng <amosng1@gmail.com>
##
# Get first line
total_i, total_s = input().split(' ')
total_i = int(total_i)
total_s = int(total_s)

# Get integers
integers = input().split(' ')
integers = list(map(int, integers))
integers = integers[:total_i]

global_counter = 0
def subset_sum(numbers, target, partial=[]):
    s = sum(partial)

    if s == target:
        if len(partial) > 0:
            global global_counter
            global_counter += 1
    # if (target > 0 and s >= target) or (target < 0 and s <= target):
    #     return

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        subset_sum(remaining, target, partial + [n])

subset_sum(integers, total_s)
print(global_counter)
