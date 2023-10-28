#!/usr/bin/env python3
# https://www.codewars.com/kata/514b92a657cdc65150000006


def solution(number):
    counter = 0
    for item in range(0, number):
        if item % 3 == 0 or item % 5 == 0:
            counter += item
    return counter
