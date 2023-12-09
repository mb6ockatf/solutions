#!/usr/bin/env pypy3
# https://codeforces.com/contest/1896/problem/A
datas = int(input())
while datas != 0:
    datas -= 1
    length = int(input())
    seq = [int(k) for k in input().split()]
    if min(seq) != seq[0]:
        print("no")
    else:
        print("yes")
