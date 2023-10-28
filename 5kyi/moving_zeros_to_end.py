#!/usr/bin/env python3
# https://www.codewars.com/kata/52597aa56021e91c93000cb0


def move_zeros(lst: list):
    result = []
    zeros = 0
    for element_index in range(len(lst)):
        element = lst[element_index]
        if element != 0:
            result.append(element)
        else:
            zeros += 1
    result.extend([0 for _ in range(zeros)])
    return result
