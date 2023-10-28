#!/usr/bin/env python3
# https://www.codewars.com/kata/526571aae218b8ee490006f4
def count_bits(n):
    return str(bin(n)[2:]).count("1")
