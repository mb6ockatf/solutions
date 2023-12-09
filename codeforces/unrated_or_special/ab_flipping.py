#!/usr/bin/env pypy3
# https://codeforces.com/contest/1896/problem/B
datas = int(input())
while datas:
    counter = 0
    datas -= 1
    length = int(input())
    performed = [True for _ in range(length)]
    data = list(input())
    changed = True
    while changed:
        changed = False
        for index in range(len(data) - 1, 0, -1):
            if (
                data[index] == "B"
                and data[index - 1] == "A"
                and performed[index]
            ):
                changed = True
                performed[index] = False
                data[index] = "A"
                data[index - 1] = "B"
                counter += 1
    print(counter)
