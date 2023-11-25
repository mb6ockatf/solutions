#!/usr/bin/env pypy3
# https://codeforces.com/problemset/problem/1/A
from math import ceil

n, m, a = [int(k) for k in input().split()]
print(ceil(m / a) * ceil(n / a))
