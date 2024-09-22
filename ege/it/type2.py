#!/usr/bin/env python3
from itertools import product, permutations


def convert(data: list) -> list:
    for i in range(len(data)):
        data[i] = int(data[i])
    return data


# -----------------------------------------------------------------------------
def f_64932(w: bool, x: bool, y: bool, z: bool) -> bool:
    return ((x == z) <= ((not y) or w)) == (not ((w <= z) or (x <= y)))


def task_64932():
    print("z y x w")
    for w, x, y, z in product([True, False], repeat=4):
        if f_64932(w, x, y, z):
            print(*convert([z, y, x, w]))


# -----------------------------------------------------------------------------
def f_68503(w: bool, x: bool, y: bool, z: bool) -> bool:
    return (not (x <= z)) or (y == w) or y


def task_68503():
    print("z x y w")
    for w, x, y, z in product([True, False], repeat=4):
        if f_68503(w, x, y, z):
            continue
        print(*convert([z, x, y, w]))


# -----------------------------------------------------------------------------
def f_38534(w: bool, x: bool, y: bool, z: bool) -> bool:
    return (not (y <= (x == w))) and (x <= x)


def task_38534():
    print("w x y z")
    for w, x, y, z in product([True, False], repeat=4):
        if f_38534(w, x, y, z):
            print(*convert([w, x, y, z]))


# -----------------------------------------------------------------------------
def f_18483(w: bool, x: bool, y: bool, z: bool) -> bool:
    return (y <= w) == (x <= (not z)) and (x or w)


def task_18483():
    lines = []
    print("y z w x F")
    for w, x, y, z in product([True, False], repeat=4):
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
    for w, x, y, z in product([True, False], repeat=4):
        if f_28677(w, x, y, z):
            print(*convert([z, y, x, w]))


# -----------------------------------------------------------------------------
def f_18430(w: bool, x: bool, y: bool, z: bool) -> bool:
    return (x and y) or (y == z) or w


def task_18430():
    print("w z y x")
    for w, x, y, z in product([True, False], repeat=4):
        if not f_18430(w, x, y, z):
            print(*convert([w, z, y, x]))


# -----------------------------------------------------------------------------
def f_18550(w: bool, x: bool, y: bool, z: bool) -> bool:
    return ((y <= z) or ((not x) and w)) == (w == z)


def task_18550():
    lines = []
    print("z w y x F")
    for w, x, y, z in product([True, False], repeat=4):
        f = f_18550(w, x, y, z)
        container = [z, w, y, x, f]
        if f or container in lines:
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
    for w, x, y, z in product([True, False], repeat=4):
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
    for w, x, y, z in product([True, False], repeat=4):
        f = f_29187(w, x, y, z)
        if not f:
            continue
        print(*convert([x, z, w, y]))


# -----------------------------------------------------------------------------
def f_16878(w: bool, x: bool, y: bool, z: bool) -> bool:
    return (x == (not y)) <= (z == (y or w))


def task_16878():
    print("z w y x")
    for w, x, y, z in product([True, False], repeat=4):
        f = f_16878(w, x, y, z)
        if not f:
            print(*convert([z, w, y, x]))


# -----------------------------------------------------------------------------
def f_27371(w: bool, x: bool, y: bool, z: bool) -> bool:
    return ((x and not y) <= (not z or not w)) and ((w <= x) or y)


def task_27371():
    print("z y w x")
    for w, x, y, z in product([True, False], repeat=4):
        f = f_27371(w, x, y, z)
        if not f:
            print(*convert([z, y, w, x]))


# -----------------------------------------------------------------------------
def f_37137(w: bool, x: bool, y: bool, z: bool) -> bool:
    return (not w and not x) or (x == y) or z

def task_37137():
    print("y z x w")
    for w, x, y, z in product([True, False], repeat=4):
        if not f_37137(w, x, y, z):
            print(*convert([y, z, x, w]))

# -----------------------------------------------------------------------------

def f_15912(w: bool, x: bool, y: bool, z: bool) -> bool:
    return ((x <= y) == (z <= w)) or (x and w)

def task_15912():
    print("z y x w")
    data = []
    for w, x, y, z in product([True, False], repeat=4):
        if not f_15912(w, x, y, z):
            print(*convert([z, y, x, w]))

# -----------------------------------------------------------------------------

def f_18781(w: bool, x: bool, y: bool, z: bool) -> bool:
    return (not x or not y) and not (x == z) and w

def task_18781():
    print("w x y z")
    for w, x, y, z in product([True, False], repeat=4):
        if f_18781(w, x, y, z):
            print(*convert([w, x, y, z]))

# -----------------------------------------------------------------------------


def f_68274(w: bool, x: bool, y: bool, z: bool) -> bool:
    return ((y or z) <= (z and w)) == (not ((x and z)<=(w or y)))

def task_68274():
    print("w y x z")
    for w, x, y, z in product([True, False], repeat=4):
        if f_68274(w, x, y, z) == 1:
            print(*convert([w, y, x, z]))

# -----------------------------------------------------------------------------

def f_18071(w: bool, x: bool, y: bool, z: bool) -> bool:
    return (x and not y) or (y == z) or not w

def task_18071():
    print("x w z y")
    for w, x, y, z in product([True, False], repeat=4):
        if not f_18071(w, x, y, z):
            print(*convert([x, w, z, y]))

# -----------------------------------------------------------------------------

def f_48450(w: bool, x: bool, y: bool, z: bool) -> bool:
    return (w <= (y == z)) and (y == (z <= x))

def task_48450():
    print("z w y x f")
    for w, x, y, z in product([True, False], repeat=4):
        f = f_48450(w, x, y, z)
        if not f and [w, x, y, z] != [True, True, True, True]:
            print(*convert([z, w, y, x, f]))

# -----------------------------------------------------------------------------

def f_14763(x: bool, y: bool, z: bool) -> bool:
    return (x or y) <= (y == z)

def task_14763():
    print("z x y")
    for x, y, z in product([True, False], repeat=3):
        if not f_14763(x, y, z):
            print(*convert([z, x, y]))

# -----------------------------------------------------------------------------

def f_70529(w: bool, x: bool, y: bool, z: bool) -> bool:
    return ((w <= y) <= x) or not z

def task_70529():
    print("z y w x")
    for w, x, y, z in product([True, False], repeat=4):
        if not f_70529(w, x, y, z):
            print(*convert([z, y, w, x]))

# -----------------------------------------------------------------------------

def f_39231(w: bool, x: bool, y: bool, z: bool) -> bool:
    return (not z == y) <= ((w and not x) == (y and x))

def task_39231():
    print("z w x y")
    for w, x, y, z in product([True, False], repeat=4):
        if not f_39231(w, x, y, z):
            print(*convert([z, w, x, y]))

# -----------------------------------------------------------------------------

def f_63018(u: bool, w: bool, x: bool, y: bool, z: bool) -> bool:
    return ((x <= y) and (z == (not w))) <= (u == (x or z))

def task_63018():
    print("w z y x u")
    for u, w, x, y, z in product([True, False], repeat=5):
        if not f_63018(u, w, x, y, z):
            print(*convert([w, z, y, x, u]))

if __name__ == "__main__":
    task_63018()
