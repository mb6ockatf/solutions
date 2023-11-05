#!/usr/bin/env pypy3
# https://codeforces.com/problemset/problem/158/A
n, k = [int(k) for k in input().split()]
contestants = [int(i) for i in input().split()]
counter = 0
constraint = contestants[k - 1]
for value in contestants:
    if value < constraint or value < 1:
        break
    counter += 1
print(counter)
