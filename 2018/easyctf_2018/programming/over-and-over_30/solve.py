#! /usr/bin/env python3
##
# Created for EasyCTF 2018_Over and Over
# By Amos (LFlare) Ng <amosng1@gmail.com>
##
times=int(input())
output=""
for i in range(times):
    output+="over and "
print(output.strip("and "))
