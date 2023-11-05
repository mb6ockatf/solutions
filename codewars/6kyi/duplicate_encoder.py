#!/usr/bin/env python3
# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c


def duplicate_encode(word: str):
    word = word.lower()
    result = ""
    for element in word:
        if word.count(element) > 1:
            result += ")"
        else:
            result += "("
    return result
