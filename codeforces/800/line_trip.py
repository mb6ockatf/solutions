#!/usr/bin/env pypy3
# https://codeforces.com/problemset/problem/1901/A
datas = int(input())
while datas != 0:
    datas -= 1
    stations_number, destination = [int(k) for k in input().split()]
    stations_coords = [0] + [int(k) for k in input().split()]
    while destination < stations_coords[-1]:
        stations_coords.pop(-1)
    stations_coords.append(2 * destination - stations_coords[-1])
    i = 0
    maximal = 0
    while i < len(stations_coords) - 1:
        result = abs(stations_coords[i] - stations_coords[i + 1])
        maximal = result if result > maximal else maximal
        i += 1
    print(maximal)
