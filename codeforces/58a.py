#!/usr/bin/env python3
s, score = input(), 0
for element in s:
    if score == 0 and element == "h":
        score += 1
    elif score == 1 and element == "e":
        score += 1
    elif score in (2, 3) and element == "l":
        score += 1
    elif score == 4 and element == "o":
        print("YES")
        exit(0)
print("NO")

