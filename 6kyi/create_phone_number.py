#!/usr/bin/env python3
# https://www.codewars.com/kata/525f50e3b73515a6db000b83

def create_phone_number(n: list) -> str:
    n = "".join([str(character) for character in n])
    return f"({n[0:3]}) {n[3:6]}-{n[6:]}"