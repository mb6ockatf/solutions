#!/usr/bin/env python3
# https://www.codewars.com/kata/526dbd6c8c0eb53254000110

"""
def alphanumeric(password: str) -> bool:
    if password.isalnum() and len(password) > 0 and not " " in password and not "_" in password:
        return True
    return False
"""

def alphanumeric(password: str) -> bool:
    return password.isalnum()