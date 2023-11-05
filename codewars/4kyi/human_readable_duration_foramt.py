#!/usr/bin/env python3
# https://www.codewars.com/kata/52742f58faf5485cae000b9a

from math import floor as round


def format_duration(seconds: int):
    if seconds == 0:
        return "now"
    time = dict()
    years = seconds / 31536000
    if years >= 1:
        value = round(years)
        time["years"] = value
        seconds -= value * 31536000
    days = seconds / 86400
    if days >= 1:
        value = round(days)
        time["days"] = value
        seconds -= value * 86400
    hours = seconds / 3600
    if hours >= 1:
        value = round(hours)
        time["hours"] = value
        seconds -= value * 3600
    minutes = seconds / 60
    if minutes >= 1:
        value = round(minutes)
        time["minutes"] = value
        seconds -= value * 60
    time["seconds"] = seconds
    buffer = []
    for name, value in time.items():
        if value != 0:
            if value == 1:
                name = name[:-1]
            message = f"{str(value)} {name}"
            buffer.append(message)
    newbuffer = ", ".join(buffer[:-1])
    if len(buffer) > 1:
        newbuffer += " and " + buffer[-1]
    else:
        newbuffer = buffer[-1]
    return newbuffer
