#!/usr/bin/env pypy3
# https://codeforces.com/problemset/problem/282/A
n, x = int(input()), 0
while n:
    n -= 1
    command = input()
    if command == "++X" or command == "X++":
        x += 1
    else:
        x -= 1
print(x)
