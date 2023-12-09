# https://codeforces.com/contest/1907/problem/A
y_cells = tuple(range(1, 9))
x_cells = "abcdefgh"
tests = int(input())
while tests != 0:
    tests -= 1
    data = input()
    x, y = data[0], data[1]
    for element in range(len(y_cells)):
        if str(y_cells[element]) == y:
            continue
        print(x + str(y_cells[element]))
    for element in range(len(x_cells)):
        if x_cells[element] == x:
            continue
        print(x_cells[element] + y)
