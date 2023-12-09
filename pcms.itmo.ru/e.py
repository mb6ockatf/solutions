#!/usr/bin/env python3
a, b, c, d = list(map(int, input().split()))
variants = [[(a, b), (c, d)], [(a, d), (c, b)], [(a, c), (b, d)]]
max_sum = float("-inf")
for variant in variants:
    s1, s2 = variant[0], variant[1]
    total = s1[0] * s1[1] + s2[0] * s2[1]
    if total > max_sum:
        max_sum = total
print(max_sum)
