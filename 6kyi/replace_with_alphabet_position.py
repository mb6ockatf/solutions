#!/usr/bin/env python3
# https://www.codewars.com/kata/546f922b54af40e1e90001da
from string import ascii_lowercase


def alphabet_position(text: str):
    text = text.lower()
    result = []
    for element in text:
        if element == " ":
            result.append(" ")
            continue
        count = 0
        for letter in ascii_lowercase:
            if element == letter:
                result.append(str(count + 1))
            count += 1
    return " ".join(result)
