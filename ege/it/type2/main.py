#!/usr/bin/env pypy3
ALL_SOLUTIONS = set()


class Solution:
    def __init__(self, identifier: int, program: callable):
        self.identifier = identifier
        self.program = program

    def __str__(self) -> str:
        self.program()
        return ""


def task_15912():
    print("w x y z")
    for w in (0, 1):
        for x in (0, 1):
            for z in (0, 1):
                for y in (0, 1):
                    f = ((x <= y) == (z <= w)) or (x and w)
                    if not f:
                        print(w, x, y, z)


ALL_SOLUTIONS.add(Solution(15912, task_15912))


def task_18614():
    print("w x y z F")
    for w in (0, 1):
        for x in (0, 1):
            for y in (0, 1):
                for z in (0, 1):
                    f = bool(
                        ((w <= (not x)) == (z <= y)) and (y or w)
                    )
                    print(w, x, y, z, f)


ALL_SOLUTIONS.add(Solution(18614, task_18614))


def task_28538():
    print("w x y z")
    for w in (0, 1):
        for x in (0, 1):
            for y in (0, 1):
                for z in (0, 1):
                    f = ((x and y) <= ((not z) or w)) and (
                        ((not w) <= x) or (not y)
                    )
                    if f == 0:
                        print(w, x, y, z)


ALL_SOLUTIONS.add(Solution(28538, task_28538))


def task_45236():
    print("w x y z")
    for x in (0, 1):
        for w in (0, 1):
            for y in (0, 1):
                for z in (0, 1):
                    f = not (x <= w) or (y == z) or y
                    if f == 0:
                        print(w, x, y, z)


ALL_SOLUTIONS.add(Solution(45236, task_45236))


def task_47206():
    print("w x y z")
    for w in (0, 1):
        for x in (0, 1):
            for y in (0, 1):
                for z in (0, 1):
                    if not (not (y <= x) or (z <= w) or (not z)):
                        print(w, x, y, z)


ALL_SOLUTIONS.add(Solution(47206, task_47206))

if __name__ == "__main__":
    task_number = int(input())
    for element in ALL_SOLUTIONS:
        if element.identifier == task_number:
            print(element, end="")
            break
