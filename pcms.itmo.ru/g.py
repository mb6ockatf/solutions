#!/usr/bin/env python3
def count_odd_sum_partitions(n):
    def inside(target, max_odd):
        if target == 0:
            return 1
        elif target < 0 or max_odd <= 0:
            return 0
        else:
            return inside(target - max_odd, max_odd) + inside(
                target, max_odd - 2
            )

    return inside(n, n if n % 2 != 0 else n - 1)


print(count_odd_sum_partitions(int(input())))
