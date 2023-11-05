#!/usr/bin/env python3
# https://www.codewars.com/kata/54d496788776e49e6b00052f


def sum_for_list(lst: list) -> list:
    answer = []
    s = set()
    for i in range(len(lst)):
        temp = abs(lst[i])
        divisor = 2
        while temp > 1:
            if temp % divisor == 0:
                s.add(divisor)
                temp /= divisor
            else:
                divisor += 1
    for number in s:
        buffer = 0
        for i in range(len(lst)):
            if lst[i] % number == 0:
                buffer += lst[i]
        answer.append([number, buffer])
    return sorted(answer)
