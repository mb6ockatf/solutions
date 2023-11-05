#!/usr/bin/env python3
# https://www.codewars.com/kata/5264d2b162488dc400000001


def spin_words(sentence: str) -> str:
    sentence = sentence.split()
    result = []
    for word in sentence:
        if len(word) > 4:
            result.append(word[::-1])
        else:
            result.append(word)
    return " ".join(result)
