#!/usr/bin/env pypy3
# https://codeforces.com/problemset/problem/231/A
n = int(input())
counter = 0
for _ in range(n):
    if sum([int(k) for k in input().split()]) >= 2:
        counter += 1
print(counter)
