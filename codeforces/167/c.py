#!/usr/bin/env pypy3

def proceed():
    n = int(input())
    filma = [*(map(int, input().split()))]
    filmb = [*(map(int, input().split()))]
    for i in range(n):
        if filma[i] == filmb[i] == 0:
            filma[i] = "aboba"
            filmb[i] = "aboba"
    filma = list(filter(lambda x: x != "aboba", filma))
    filmb = list(filter(lambda x: x != "aboba", filmb))
    if sum(filma) > sum(filmb):
        better = filma
        worse = filmb
    else:
        better = filmb
        worse = filma
    while sum(worse) < sum(better):
        changed = False
        for i in range(n):
            if better[i] > worse[i]:
                worse[i], better[i] = better[i], worse[i]
                changed = True
                break
        if not changed:
            break
    return sum(worse)

for _ in range(int(input())):
    print(proceed())

