#!/usr/bin/env pytho3


def f27755(x: int, y: int, h: int) -> int:
    if h == 4 and x + y >= 61:
        return True
    elif h == 4 and x + y < 61:
        return False
    elif h < 4 and x + y >= 61:
        return False
    if h % 2 != 0:
        return (
            f27755(x + 1, y, h + 1)
            or f27755(x * 4, y, h + 1)
            or f27755(x, y + 1, h + 1)
            or f27755(x, y * 4, h + 1)
        )
    else:
        return (
            f27755(x + 1, y, h + 1)
            and f27755(x * 4, y, h + 1)
            and f27755(x, y + 1, h + 1)
            and f27755(x, y * 4, h + 1)
        )


def task_27755() -> int:
    for S in range(1, 58):
        if f(3, S, 1):
            return S


def f27792(x: int, y: int, h: int) -> bool:
    if h in (3, 5) and x + y >= 62:
        return True
    elif h == 5 and x + y < 62:
        return False
    elif h < 5 and x + y >= 62:
        return False
    if h % 2 == 0:
        return (
            f27792(x + 1, y, h + 1)
            or f27792(x * 2, y, h + 1)
            or f27792(x, y + 1, h + 1)
            or f27792(x, y * 2, h + 1)
        )
    else:
        return (
            f(x + 1, y, h + 1)
            and f(x * 2, y, h + 1)
            and f(x, y + 1, h + 1)
            and f(x, y * 2, h + 1)
        )


def f27792(x: int, y: int, h: int) -> bool:
    if h == 3 and x + y >= 62:
        return True
    elif h == 3 and x + y > 62:
        return 0
    elif h < 3 and x + y <= 62:
        return False
    if h % 2 == 0:
        return (
            f27792(x + 1, y, h + 1)
            or f27792(x * 2, y, h + 1)
            or f27792(x, y + 1, h + 1)
            or f27792(x, y * 2, h + 1)
        )
    else:
        return (
            f27792(x + 1, y, h + 1)
            and f27792(x * 2, y, h + 1)
            and f27792(x, y + 1, h + 1)
            and f27792(x, y * 2, h + 1)
        )


def task_27792() -> int:
    for S in range(1, 52):
        if f(10, S, 1) == 1:
            return S


def f27756(x: int, y: int, h: int) -> int:
    if (h == 3 or h == 5) and x + y >= 61:
        return 1
    elif h == 5 and x + y < 61:
        return 0
    elif x + y >= 61 and h < 5:
        return 0
    else:
        if h % 2 == 0:
            return (
                f27756(x + 1, y, h + 1)
                or f27756(x, y + 1, h + 1)
                or f27756(x * 4, y, h + 1)
                or f27756(x, y * 4, h + 1)
            )
        else:
            return (
                f27756(x + 1, y, h + 1)
                and f27756(x, y + 1, h + 1)
                and f27756(x * 4, y, h + 1)
                and f27756(x, y * 4, h + 1)
            )


def f27756_1(x: int, y: int, h: int) -> int:
    if h == 3 and x + y >= 61:
        return 1
    elif h == 3 and x + y < 61:
        return 0
    elif x + y >= 61 and h < 3:
        return 0
    else:
        if h % 2 == 0:
            return (
                f27756_1(x + 1, y, h + 1)
                or f27756_1(x, y + 1, h + 1)
                or f27756_1(x * 4, y, h + 1)
                or f27756_1(x, y * 4, h + 1)
            )
        else:
            return (
                f27756_1(x + 1, y, h + 1)
                and f27756_1(x, y + 1, h + 1)
                and f27756_1(x * 4, y, h + 1)
                and f27756_1(x, y * 4, h + 1)
            )


def task_27756() -> list:
    answer: list = []
    for x in range(1, 58):
        if f27756(x, 3, 1) == 1:
            answer.append(x)
    for x in range(1, 58):
        if f27756_1(x, 3, 1) == 1:
            answer.append(x)
    return answer


def f27747(x: int, h: int) -> bool:
    if 52 <= x and h == 3:
        return True
    elif h == 3 and 52 > x or h < 3 and 52 <= x:
        return False
    else:
        h += 1
        return f27747(x + 1, h) or f27747(x + 4, h) or f27747(x * 2, h)


def task_27747() -> int:
    for S in range(1, 50):
        if f27747(S, 1):
            return S


def f27790(x: int, y: int, h: int) -> bool:
    if h == 4 and x + y >= 62:
        return True
    elif h == 3 and x + y < 62:
        return False
    elif h < 3 and x + y >= 62:
        return False
    if h % 2 == 0:
        return (
            f27790(x + 1, y, h + 1)
            or f27790(x * 2, y, h + 1)
            or f27790(x, y + 1, h + 1)
            or f27790(x, y * 2, h + 1)
        )
    else:
        return (
            f27790(x + 1, y, h + 1)
            or f27790(x * 2, y, h + 1)
            or f27790(x, y + 1, h + 1)
            or f27790(x, y * 2, h + 1)
        )


def task_27790() -> int:
    for S in range(1, 52):
        if f27790(10, S, 1) == 1:
            return S


def f27791(x: int, y: int, h: int) -> bool:
    if h == 4 and x + y >= 62:
        return True
    elif h == 4 and x + y < 62:
        return False
    elif h < 4 and x + y >= 62:
        return False
    if h % 2 != 0:
        return (
            f27791(x + 1, y, h + 1)
            or f27791(x * 2, y, h + 1)
            or f27791(x, y + 1, h + 1)
            or f27791(x, y * 2, h + 1)
        )
    else:
        return (
            f27791(x + 1, y, h + 1)
            and f27791(x * 2, y, h + 1)
            and f27791(x, y + 1, h + 1)
            and f27791(x, y * 2, h + 1)
        )


def task_27791() -> int:
    for S in range(1, 52):
        if f27791(10, S, 1) == 1:
            return S


def f27750(x: int, y: int, h: int) -> int:
    if (h == 3 or h == 5) and x + y >= 82:
        return 1
    elif h == 5 and x + y < 82:
        return 0
    elif x + y >= 82 and h < 5:
        return 0
    else:
        if h % 2 == 0:
            return (
                f27750(x + 1, y, h + 1)
                or f27750(x, y + 1, h + 1)
                or f27750(x * 4, y, h + 1)
                or f27750(x, y * 4, h + 1)
            )
        else:
            return (
                f27750(x + 1, y, h + 1)
                and f27750(x, y + 1, h + 1)
                and f27750(x * 4, y, h + 1)
                and f27750(x, y * 4, h + 1)
            )


def f27750_1(x: int, y: int, h: int) -> int:
    if h == 3 and x + y >= 82:
        return 1
    elif h == 3 and x + y < 82:
        return 0
    elif x + y >= 82 and h < 3:
        return 0
    else:
        if h % 2 == 0:
            return (
                f27750_1(x + 1, y, h + 1)
                or f27750_1(x, y + 1, h + 1)
                or f27750_1(x * 4, y, h + 1)
                or f27750_1(x, y * 4, h + 1)
            )
        else:
            return (
                f27750_1(x + 1, y, h + 1)
                and f27750_1(x, y + 1, h + 1)
                and f27750_1(x * 4, y, h + 1)
                and f27750_1(x, y * 4, h + 1)
            )


def task_27750() -> int:
    for x in range(1, 78):
        if f27750(x, 4, 1) == 1:
            return x
    for x in range(1, 78):
        if f27750_1(x, 4, 1) == 1:
            return x


def f27754(x: int, y: int, h: int) -> bool:
    if h == 3 and x + y >= 61:
        return True
    elif h == 3 and x + y < 61:
        return 0
    elif h < 3 and x + y >= 61:
        return False
    if h % 2 == 0:
        return (
            f27754(x + 1, y, h + 1)
            or f27754(x * 4, y, h + 1)
            or f27754(x, y + 1, h + 1)
            or f27754(x, y * 4, h + 1)
        )
    else:
        return (
            f27754(x + 1, y, h + 1)
            or f27754(x * 4, y, h + 1)
            or f27754(x, y + 1, h + 1)
            or f27754(x, y * 4, h + 1)
        )


def task_27754() -> int:
    for S in range(1, 58):
        if f(3, S, 1) == 1:
            return S
