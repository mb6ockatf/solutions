#!/usr/bin/env python3
# https://www.codewars.com/kata/638b042bf418c453377f28ad

import itertools


def guess(n):
    if n == -1:
        guess.remaining_codes = list(itertools.permutations(range(10), 4))
        guess.prev_guess = guess.remaining_codes[0]
    else:
        guess.remaining_codes = [
            code
            for code in guess.remaining_codes
            if sum(a == b for a, b in zip(code, guess.prev_guess)) == n
        ]
        guess.prev_guess = guess.remaining_codes[0]
    return list(guess.prev_guess)


guess.remaining_codes = None
guess.prev_guess = None
