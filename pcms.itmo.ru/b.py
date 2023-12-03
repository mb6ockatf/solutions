def to_balanced_ternary(n):
    result = ''
    while n != 0:
        remainder = n % 3
        n //= 3
        if remainder == 2:
            n += 1
            result = '$' + result
        elif remainder == 1:
            result = '1' + result
        else:
            result = '0' + result
    if result == '':
        result = '0'
    return result


print(to_balanced_ternary(int(input())))