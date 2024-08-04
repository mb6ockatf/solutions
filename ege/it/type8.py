#!/usr/bin/env python
from itertools import permutations, product


def task_59746() -> int:
    result: int = 0
    alphabet: str = "0123456789"
    for i in range(1, 11):
        for aboba in permutations(alphabet, i):
            data: str = "".join(aboba)
            if data[0] == "0" or data[-1] not in ("0", "5"):
                continue
            result += 1
    return result + 1


def task_10473() -> int:
    alphabet: str = "1234"
    result: int = 0
    for attempt in product(alphabet, repeat=5):
        if attempt.count("1") != 2:
            continue
        result += 1
    return result


def task_7306() -> int:
    result: int = 0
    alphabet: str = "abcdef"
    for aboba in product(alphabet, repeat=5):
        if aboba[0] == "a" and aboba[1] == "b":
            result += 1
    return result


def task_18491() -> int:
    result: int = 0
    alphabet: str = "ОЛЬГА"
    for aboba in permutations(alphabet):
        if aboba[0] == "Ь" or aboba[aboba.index("Ь") - 1] in ("А", "О"):
            continue
        result += 1
    return result


def task_59742() -> int:
    counter: int = 0
    for i in range(1000, 10000):
        data: str = str(i)
        if (
            (int(data[0]) % 2 == 0) == (int(data[1]) % 2 == 0)
            or (int(data[1]) % 2 == 0) == (int(data[2]) % 2 == 0)
            or (int(data[2]) % 2 == 0) == (int(data[3]) % 2 == 0)
            or len(set(data)) != 4
        ):
            continue
        counter += 1
    return counter


def task_59745() -> int:
    alphabet: str = "АГИЛМОРТ"
    is_even: bool = False
    counter: int = 0
    for aboba in product(alphabet, repeat=5):
        if not is_even:
            if aboba[0] != "Г" and aboba.count("И") >= 2:
                counter += 1
            is_even = True
        else:
            is_even = False
    return counter


def task_16037() -> int:
    counter: int = 0
    alphabet: str = "ЗИМА"
    for aboba in product(alphabet, repeat=5):
        if aboba.count("И") + aboba.count("А") != 1:
            continue
        counter += 1
    return counter


if __name__ == "__main__":
    print(task_16037())
