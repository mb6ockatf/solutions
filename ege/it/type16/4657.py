#!/usr/bin/env python3
def f(n: int) -> int:
    if n == 1:
        return 1
    return 2 * g(n - 1) + 5 * n


def g(n: int) -> int:
    if n == 1:
        return 1
    return f(n - 1) + 2 * n


if __name__ == "__main__":
    print(f(4) + g(4))
