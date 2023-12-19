#!/usr/bin/env pypy3

def f(x, h) -> bool:
    if 52 <= x and h == 3:
        return True
    elif h == 3 and 52 > x or h < 3 and 52 <= x:
        return False
    else:
        h += 1
        return f(x + 1, h) or f(x + 4, h) or f(x * 2, h)

for S in range(1, 50):
    if f(S, 1):
        print(S)
        break