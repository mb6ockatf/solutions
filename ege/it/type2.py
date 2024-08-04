#!/usr/bin/env python3


def convert(data: list) -> list:
    for i in range(len(data)):
        data[i] = int(data[i])
    return data


# -----------------------------------------------------------------------------
def f_64932(w: bool, x: bool, y: bool, z: bool) -> bool:
    return ((x == z) <= ((not y) or w)) == (not ((w <= z) or (x <= y)))


def task_64932():
    print("z y x w")
    for w in (False, True):
        for x in (False, True):
            for y in (False, True):
                for z in (False, True):
                    if not f_64932(w, x, y, z):
                        continue
                    print(*convert([z, y, x, w]))


# -----------------------------------------------------------------------------
def f_68503(w: bool, x: bool, y: bool, z: bool) -> bool:
    return (not (x <= z)) or (y == w) or y


def task_68503():
    print("z x y w")
    for w in (False, True):
        for x in (False, True):
            for y in (False, True):
                for z in (False, True):
                    if f_68503(w, x, y, z):
                        continue
                    print(*convert([z, x, y, w]))


# -----------------------------------------------------------------------------
def f_38534(w: bool, x: bool, y: bool, z: bool) -> bool:
    return (not (y <= (x == w))) and (x <= x)


def task_38534():
    print("w x y z")
    for w in (False, True):
        for x in (False, True):
            for y in (False, True):
                for z in (False, True):
                    if not f_38534(w, x, y, z):
                        continue
                    print(*convert([w, x, y, z]))


# -----------------------------------------------------------------------------
def f_18483(w: bool, x: bool, y: bool, z: bool) -> bool:
    return (y <= w) == (x <= (not z)) and (x or w)


def task_18483():
    lines = []
    print("y z w x F")
    for w in (False, True):
        for x in (False, True):
            for y in (False, True):
                for z in (False, True):
                    f = f_18483(w, x, y, z)
                    container = [y, z, w, x, f]
                    #                   if (not f) and (container.count(True) == 3):
                    #                       print("SELECTED:", *container)
                    if container not in lines and f:
                        lines.append(container)
    for container in lines:
        print(*convert(container))


# -----------------------------------------------------------------------------
def f_28677(w: bool, x: bool, y: bool, z: bool) -> bool:
    return ((x <= y) or (y == w)) and ((x or z) == w)


def task_28677():
    print("z y x w")
    for w in (False, True):
        for x in (False, True):
            for y in (False, True):
                for z in (False, True):
                    if not f_28677(w, x, y, z):
                        continue
                    print(*convert([z, y, x, w]))


# -----------------------------------------------------------------------------
def f_18430(w: bool, x: bool, y: bool, z: bool) -> bool:
    return (x and y) or (y == z) or w


def task_18430():
    print("w z y x")
    for w in (False, True):
        for x in (False, True):
            for y in (False, True):
                for z in (False, True):
                    if f_18430(w, x, y, z):
                        continue
                    print(*convert([w, z, y, x]))


# -----------------------------------------------------------------------------
def f_18550(w: bool, x: bool, y: bool, z: bool) -> bool:
    return ((y <= z) or ((not x) and w)) == (w == z)


def task_18550():
    lines = []
    print("z w y x F")
    for w in (False, True):
        for x in (False, True):
            for y in (False, True):
                for z in (False, True):
                    f = f_18550(w, x, y, z)
                    container = [z, w, y, x, f]
                    if not f or container in lines:
                        continue
                    lines.append(container)
    for container in lines:
        print(*convert(container))


# -----------------------------------------------------------------------------
def f_27260(w: bool, x: bool, y: bool, z: bool) -> bool:
    return ((x or (not y)) and ((not z) == w)) <= (y and z)


def task_27260():
    print("y z w x")
    lines = []
    for w in (False, True):
        for x in (False, True):
            for y in (False, True):
                for z in (False, True):
                    f = f_27260(w, x, y, z)
                    container = [y, z, w, x]
                    if f or container in lines:
                        continue
                    lines.append(container)
    for container in lines:
        print(*convert(container))


# -----------------------------------------------------------------------------
def f_29187(w: bool, x: bool, y: bool, z: bool) -> bool:
    return (w <= y) and ((not y) == x) and (x or z)


def task_29187():
    print("x z w y")
    for w in (False, True):
        for x in (False, True):
            for y in (False, True):
                for z in (False, True):
                    f = f_29187(w, x, y, z)
                    if not f:
                        continue
                    print(*convert([x, z, w, y]))


# -----------------------------------------------------------------------------
def f_16878(w: bool, x: bool, y: bool, z: bool) -> bool:
    return (x == (not y)) <= (z == (y or w))


def task_16878():
    print("z w y x")
    for w in (False, True):
        for x in (False, True):
            for y in (False, True):
                for z in (False, True):
                    f = f_16878(w, x, y, z)
                    if f:
                        continue
                    print(*convert([z, w, y, x]))


# -----------------------------------------------------------------------------
def f_27371(w: bool, x: bool, y: bool, z: bool) -> bool:
    return ((x and not y) <= (not z or not w)) and ((w <= x) or y)


def task_27371():
    print("z y w x")
    for w in (False, True):
        for x in (False, True):
            for y in (False, True):
                for z in (False, True):
                    f = f_27371(w, x, y, z)
                    if f:
                        continue
                    print(*convert([z, y, w, x]))


if __name__ == "__main__":
    task_27371()
