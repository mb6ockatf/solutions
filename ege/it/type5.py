#!/usr/bin/env python3


def task_9190() -> int:
    counter: int = 0
    for number in range(100, 999):
        data: str = str(number)
        new_components = [int(data[0]) + int(data[1])]
        new_components.append(int(data[1]) + int(data[2]))
        new_components.sort()
        new_components = [str(k) for k in new_components]
        new_number = "".join(new_components)
        if new_number == "1216":
            counter += 1
    return counter


def task_8094() -> int:
    for i in range(100):
        data: str = str(bin(i))[2:]
        for _ in range(2):
            data += str(sum([int(j) for j in data]) % 2)
        r: int = int(data, 2)
        if r > 43:
            return r


def task_9298() -> int:
    counter: int = 0
    for i in range(100, 1000):
        data: str = str(i)
        a: int = int(data[0]) + int(data[1])
        b: int = int(data[1]) + int(data[2])
        if a > b:
            r: str = str(a) + str(b)
        else:
            r: str = str(b) + str(a)
        if r == "1715":
            counter += 1
    return counter


def task_11262() -> int:
    for i in range(1000, 10000):
        date: str = str(i)
        a: int = int(date[0]) + int(date[1])
        b: int = int(date[1]) + int(date[2])
        c: int = int(date[2]) + int(date[3])
        container: list = [a, b, c]
        container.remove(min(container))
        container.sort()
        result: str = str(container[0]) + str(container[1])
        if result == "1517":
            return i


def task_33750() -> int:
    for n in range(2, 100):
        data: str = str(bin(n))[2:]
        buffer: str = data[1]
        data = data[:-1] + buffer + buffer
        result: int = int(data, 2)
        if result > 76:
            return n


def task_28897() -> int:
    for n in range(1, 100):
        data: str = str(bin(n))[2:]
        for _ in range(2):
            data += str(sum([int(j) for j in data]) % 2)
        r: int = int(data, 2)
        if r > 125:
            return n


def task_10380() -> int:
    for i in range(9999, 999, -1):
        data: str = str(i)
        a: int = int(data[0]) + int(data[1])
        b: int = int(data[1]) + int(data[2])
        c: int = int(data[2]) + int(data[3])
        container: list = [a, b, c]
        container.remove(min(container))
        container.sort()
        result: str = str(container[0]) + str(container[1])
        if result == "1517":
            return i


def task_27291() -> int:
    result: int = 0
    for i in range(1, 10000):
        data: str = str(bin(i))[2:]
        for _ in range(2):
            data += str(sum([int(j) for j in data]) % 2)
        current: int = int(data, 2)
        if current >= 90:
            return result
        if current > result:
            result = current


def task_13617() -> int:
    for i in range(100, 1000):
        data: str = str(i)
        a: int = int(data[0]) * int(data[1])
        b: int = int(data[1]) * int(data[2])
        container: list = [a, b]
        container.sort(reverse=True)
        result: str = str(container[0]) + str(container[1])
        if result == "123":
            return i


def task_13536() -> int:
    counter: int = 0
    for i in range(1000, 10000):
        if not all([int(j) % 2 != 0 for j in str(i)]):
            continue
        data: str = str(i)
        a: int = int(data[0]) + int(data[1])
        b: int = int(data[2]) + int(data[3])
        container: list = [a, b]
        container.sort()
        if str(container[0]) + str(container[1]) == "414":
            counter += 1
    return counter


def task_69883() -> int:
    for i in range(30, 0, -1):
        data: str = str(bin(i))[2:]
        if sum([int(j) for j in data]) % 2 == 0:
            data = "10" + data[2:] + "0"
        else:
            data = "11" + data[2:] + "1"
        if int(data, 2) < 35:
            return i


if __name__ == "__main__":
    print(task_69883())
