#!/usr/bin/env pypy3

def f(x, y, h) -> bool:
    if h == 3 and x + y >= 82:
        return True
    elif h == 3 and x + y < 82:
        return False
    elif x + y >= 82 and h < 3:
        return False
    else:
        if h % 2 == 0:
            return f(x + 1, y, h + 1) or f(x, y + 1, h + 1) or f(x * 4, y, h + 1) or f(x, y * 4, h + 1)
        else:
            return f(x + 1, y, h + 1) or f(x, y + 1, h + 1) or f(x * 4, y, h + 1) or f(x, y * 4, h + 1)


for S in range(1, 78):
    if f(4, S, 1) == 1:
        print(S)
        break