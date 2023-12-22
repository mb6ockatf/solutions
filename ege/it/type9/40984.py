#!/usr/bin/env python3
from csv import reader

counter = 0
with open("40984.csv", "r") as file:
    stream = reader(file)
    for line in stream:
        a, b, c = [int(k) for k in line[0].split(";")]
        s1, s2, s3 = a * b, b * c, a * c
        if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
            counter += 1
print(counter)
