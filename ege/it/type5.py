#!/usr/bin/env python3


def task_9190():
    counter = 0
    for number in range(100, 999):
        data = str(number)
        new_components = [int(data[0]) + int(data[1])]
        new_components.append(int(data[1]) + int(data[2]))
        new_components.sort()
        new_components = [str(k) for k in new_components]
        new_number = "".join(new_components)
        if new_number == "1216":
            counter += 1
    print(counter)


if __name__ == "__main__":
    task_9190()
