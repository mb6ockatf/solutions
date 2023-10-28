#!/usr/bin/env python3
# https://www.codewars.com/kata/541c8630095125aba6000c00

def digital_root(n: int) -> int:
    n = list(str(n))
    counter = 0
    for element in n:
        counter += int(element)
    while len(str(counter)) > 1:
        counter = sum([int(char) for char in str(counter)])
    return counter