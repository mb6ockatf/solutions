#!/usr/bin/env python3
# https://www.codewars.com/kata/52685f7382004e774f0001f7


def make_readable(total_seconds: int) -> str:
    hours = total_seconds // 3600
    minutes = total_seconds // 60 % 60
    seconds = total_seconds % 60
    return "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
