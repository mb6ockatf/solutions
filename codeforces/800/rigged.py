#!/usr/bin/env python3
# https://codeforces.com/contest/1879/problem/A

tests = int(input())
for _ in range(tests):
    error = False
    athletes = int(input())
    sportsmen_params = []
    for _ in range(athletes):
        strength, endurance = input().split()
        sportsmen_params.append((int(strength), int(endurance)))
    polykarp = sportsmen_params[0]
    for person in sportsmen_params[1:]:
        if person[0] >= polykarp[0] and person[1] >= polykarp[1]:
            print(-1)
            error = True
            break
    if error:
        continue
    print(polykarp[0])
