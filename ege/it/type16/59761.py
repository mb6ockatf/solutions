#!/usr/bin/env pypy3
import sys

sys.setrecursionlimit(60000)


def f(n: int) -> int:
    if n < 11:
        return 10
    return n + f(n - 1)


print(f(2124) - f(2122))
