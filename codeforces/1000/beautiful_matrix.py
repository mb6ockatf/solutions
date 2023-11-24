#!/usr/bin/env pypy
# https://codeforces.com/problemset/problem/263/A
coord_x, coord_y = 0, 0
for line_number in range(5):
    line = input()
    if not "1" in line:
        continue
    coord_y = line_number + 1
    coord_x = line.split().index("1") + 1
    break
print(abs(3 - coord_x) + abs(3 - coord_y))
