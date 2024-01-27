def f(x, y, h):
    if h == 4 and x + y >= 61:
        return True
    elif h == 4 and x + y < 61:
        return False
    elif h < 4 and x + y >= 61:
        return False
    if h % 2 != 0:
        return (
            f(x + 1, y, h + 1)
            or f(x * 4, y, h + 1)
            or f(x, y + 1, h + 1)
            or f(x, y * 4, h + 1)
        )
    else:
        return (
            f(x + 1, y, h + 1)
            and f(x * 4, y, h + 1)
            and f(x, y + 1, h + 1)
            and f(x, y * 4, h + 1)
        )


for S in range(1, 58):
    if f(3, S, 1):
        print(S)
