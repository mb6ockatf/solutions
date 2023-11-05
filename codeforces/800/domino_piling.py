#!/usr/bin/env pypy3
# https://codeforces.com/problemset/problem/50/A
m, n = map(int, input().split())
if not m % 2 or not n % 2:
    print(m * n // 2)
else:
    m -= 1
    n -= 1
    print(m * n // 2 + (m + n + 1) // 2)
