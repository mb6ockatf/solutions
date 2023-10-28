#!/usr/bin/env python3
# https://www.codewars.com/kata/54da5a58ea159efa38000836
def find_it(seq: list) -> int:
    numbers = set(seq)
    for char in numbers:
        if seq.count(char) % 2 == 1:
            return char
