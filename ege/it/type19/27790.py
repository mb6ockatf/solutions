def f(x, y, h):
    if h == 4 and x + y >= 62:
        return True
    elif h == 3 and x + y < 62:
        return False
    elif h < 3 and x + y >= 62:
        return False
    if h % 2 == 0:
        return (
            f(x + 1, y, h + 1)
            or f(x * 2, y, h + 1)
            or f(x, y + 1, h + 1)
            or f(x, y * 2, h + 1)
        )
    else:
        return (
            f(x + 1, y, h + 1)
            or f(x * 2, y, h + 1)
            or f(x, y + 1, h + 1)
            or f(x, y * 2, h + 1)
        )


for S in range(1, 52):
    if f(10, S, 1) == 1:
        print(S)
        break
