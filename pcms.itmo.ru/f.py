def max_divisors_number(n):
    max_divisors = 0
    result = 0
    for num in range(1, n + 1):
        divisors_count = 0
        for i in range(1, num + 1):
            if num % i == 0:
                divisors_count += 1
        if divisors_count > max_divisors:
            max_divisors = divisors_count
            result = num
    return result


n = int(input())
print(max_divisors_number(n))