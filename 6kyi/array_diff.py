#!/usr/bin/env python3
# https://www.codewars.com/kata/523f5d21c841566fde000009

def array_diff(a: list, b: list) -> list:
    for element in b:
        while element in a:
            a.remove(element)
    return a