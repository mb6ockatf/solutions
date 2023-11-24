#!/usr/bin/env pypy3
# https://codeforces.com/problemset/problem/339/A
expression = input().split("+")
expression.sort()
print("+".join(expression))
