#!/usr/bin/env python3
# https://www.codewars.com/kata/51ba717bb08c1cd60f00002f

def solution(args: list) -> str:
    buffer = []
    sequence = []
    for i in args:
        if len(sequence) == 0:
            sequence.append(str(i))
        elif int(sequence[-1]) + 1 == i:
            sequence.append(str(i))
        else:
            if len(sequence) < 3:
                buffer = buffer + sequence
                sequence = [str(i),]
            else:
                record = sequence[0] + "-" + sequence[-1]
                sequence = [str(i),]
                buffer.append(record)
    if len(sequence) < 3:
        buffer = buffer + sequence
    else:
        record = sequence[0] + "-" + sequence[-1]
        buffer.append(record)
    return ",".join(buffer)