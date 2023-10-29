#!/usr/bin/env python3
# https://www.codewars.com/kata/5254ca2719453dcc0b00027d

from itertools import permutations

default_permutations = permutations


def permutations(s: str):
    answer = default_permutations(s)
    result = []
    for element in answer:
        result.append("".join(element))
    result = list(set(result))
    return result
