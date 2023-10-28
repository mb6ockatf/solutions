#!/usr/bin/env python3
# https://www.codewars.com/kata/5266876b8f4bf2da9b000362

def likes(names: list) -> str:
    match len(names):
        case 0:
            result = "no one likes this"
        case 1:
            result = f"{names[0]} likes this"
        case 2:
            result = f"{names[0]} and {names[1]} like this"
        case 3:
            result = f"{names[0]}, {names[1]} and {names[2]} like this"
        case _:
            result = f"{names[0]}, {names[1]} and {len(names) - 2}"
            result += " others like this"
    return result