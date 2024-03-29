#!/usr/bin/env python3

def mix(s1: str, s2: str):
    data = dict()
    characterset = list(sorted(list(set(s1) | set(s2))))
    for character in characterset:
        occurences_s1 = s1.count(character)
        occurences_s2 = s2.count(character)
        if not (character.isalpha() and character == character.lower()):
            continue
        elif occurences_s1 <= 1 and occurences_s2 <= 1:
            continue
        if occurences_s1 > occurences_s2:
            print("1:" + character * occurences_s1)
        elif occurences_s2 > occurences_s1:
            print("2:" + character * occurences_s2)
        else:
            print("=:" + character * occurences_s1)


mix("Are they here", "yes, they are here")
