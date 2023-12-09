#!/usr/bin/env python3
from itertools import combinations


def next_combination(n, k, current_combination):
    current = tuple(int(x) for x in current_combination.split())
    all_combinations = list(combinations(range(1, n + 1), k))
    index = all_combinations.index(current)
    if index < len(all_combinations) - 1:
        next_comb = all_combinations[index + 1]
        return " ".join(str(x) for x in next_comb)
    else:
        return "-1"


n, k = list(map(int, input().split()))
current = input()

print(next_combination(n, k, current))
