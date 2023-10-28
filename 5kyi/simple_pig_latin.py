#!/usr/bin/env python3
# https://www.codewars.com/kata/520b9d2ad5c005041100000f


def pig_it(text):
    text = text.split()
    for i in range(len(text)):
        if text[i] in "?!":
            continue
        text[i] = text[i][1:] + text[i][0] + "ay"
    return " ".join(text)
