#!/usr/bin/env pypy3
# https://codeforces.com/contest/1896/problem/E
datas = int(input())
for _ in range(datas):
    length = int(input())
    a = list(map(int, input().split()))
    result = [-1] * length
    iteration = 0
    current = []
    b = 0
    while True:
        b += 1
        for i in range(length):
            if a[i] == i + 1:
                result[i] = iteration
            else:
                current.append(a[i])
        iteration += 1
        if not current:
            break
        current.insert(0, current[-1])
        current.pop(-1)
        for element in current:
            for s_ind in range(len(result)):
                if result[s_ind] == -1:
                    a[s_ind] = element
        print("A:", a)
        print("CURRENT:", current)
        print("RESULT:", result)
        break
        current = []
    print(" ".join(result))
