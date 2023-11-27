#!/usr/bin/env pypy3
# https://codeforces.com/contest/1896/problem/D
datas = int(input())
while datas != 0:
    datas -= 1
    length, queries = [int(k) for k in input().split()]
    a = list(map(int, input().split()))
    while queries != 0:
        queries -= 1
        args = input().split()
        operation = args[0]
        if operation == "1":
            param = int(args[1])
            ok = False
            for j in range(len(a)):
                summer = 0
                for k in range(j, len(a)):
                    summer += a[k]
                    if summer > param:
                        break
                    elif summer == param:
                        ok = True
                        break
                if ok:
                    break
            if ok:
                print("YES")
            else:
                print("NO")
        else:
            param1 = int(args[1])
            param2 = int(args[2])
            a[param1 - 1] = param2
