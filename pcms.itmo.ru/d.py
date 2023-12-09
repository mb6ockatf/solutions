#!/usr/bin/env python3
def min_penalty(arr):
    penalty = 0
    while len(arr) > 2:
        min_penalty_index = 1
        min_penalty_value = arr[0] * (arr[1] + arr[2])
        for i in range(1, len(arr) - 2):
            current_penalty = arr[i] * (arr[i - 1] + arr[i + 2])
            if current_penalty < min_penalty_value:
                min_penalty_value = current_penalty
                min_penalty_index = i
        penalty += min_penalty_value
        del arr[min_penalty_index]
    return penalty


n = int(input())
arr = list(map(int, input().split()))
print(min_penalty(arr))
