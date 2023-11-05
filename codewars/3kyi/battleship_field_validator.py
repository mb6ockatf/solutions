#!/usr/bin/env python3
# this solution is bad. please, never code like that
# https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7


class BoatStorage:
    def __init__(self):
        self._boats = {"4": 1, "3": 2, "2": 3, "1": 4}

    def __getitem__(self, item: str) -> int:
        return self._boats[item]

    def __setitem__(self, key: str, value: int) -> None:
        self._boats[key] = value

    def __bool__(self):
        for _element in self._boats.values():
            if _element != 0:
                print(self._boats)
                print("ABOBA")
                return False
        return True

    def keys(self):
        return list(self._boats.keys())


def check_field(field: list, a: int, b: int):
    if a > 9 or b > 9 or a < 0 or b < 0:
        return False
    return field[a][b]


def validate_battlefield(field: list) -> bool:
    _corner_conditions = (
        field[9][8] & field[8][9],
        field[0][8] & field[1][9],
        field[0][1] & field[1][0],
        field[9][1] & field[8][0],
    )
    if any(_corner_conditions):
        return False
    for row_index in range(1, 9):
        for column_index in range(1, 9):
            if not field[row_index][column_index]:
                continue
            _diagonal_conditions = (
                field[row_index - 1][column_index - 1],
                field[row_index - 1][column_index + 1],
                field[row_index + 1][column_index + 1],
                field[row_index + 1][column_index - 1],
            )
            if any(_diagonal_conditions):
                return False
    boats = BoatStorage()
    if field[0][0]:
        boat_length_counter = 1
        following_square = field[boat_length_counter][0]
        if following_square:
            while following_square:
                field[boat_length_counter][0] = 0
                boat_length_counter += 1
                following_square = field[boat_length_counter][0]
        else:
            following_square = field[0][boat_length_counter]
            while following_square:
                field[0][boat_length_counter] = 0
                boat_length_counter += 1
                following_square = field[0][boat_length_counter]
        field[0][0] = 0
        removed_boat = str(boat_length_counter)
        if removed_boat in boats.keys():
            boats[removed_boat] -= 1
        else:
            return False
    elif field[0][9]:
        boat_length_counter = 1
        following_square = field[boat_length_counter][9]
        if following_square:
            while following_square:
                field[boat_length_counter][9] = 0
                boat_length_counter += 1
                following_square = field[boat_length_counter][9]
        else:
            following_square = field[0][9 - boat_length_counter]
            while following_square:
                field[0][9 - boat_length_counter] = 0
                boat_length_counter += 1
                following_square = field[0][9 - boat_length_counter]
        field[0][9] = 0
        removed_boat = str(boat_length_counter)
        if removed_boat in boats.keys():
            boats[removed_boat] -= 1
        else:
            print(boat_length_counter)
            return False
    elif field[9][0]:
        boat_length_counter = 1
        following_square = field[9 - boat_length_counter][0]
        if following_square:
            while following_square:
                field[9 - boat_length_counter][0] = 0
                boat_length_counter += 1
                following_square = field[9 - boat_length_counter][0]
        else:
            following_square = field[9][boat_length_counter]
            while following_square:
                field[9][boat_length_counter] = 0
                boat_length_counter += 1
                following_square = field[9][boat_length_counter]
        field[9][0] = 0
        removed_boat = str(boat_length_counter)
        if removed_boat in boats.keys():
            boats[removed_boat] -= 1
        else:
            return False
    elif field[9][9]:
        boat_length_counter = 1
        following_square = field[9 - boat_length_counter][9]
        if following_square:
            while following_square:
                field[9 - boat_length_counter][9] = 0
                boat_length_counter += 1
                following_square = field[9 - boat_length_counter][9]
        else:
            following_square = field[9][9 - boat_length_counter]
            while following_square:
                field[9][9 - boat_length_counter] = 0
                boat_length_counter += 1
                following_square = field[9][9 - boat_length_counter]
        field[9][9] = 0
        removed_boat = str(boat_length_counter)
        if removed_boat in boats.keys():
            boats[removed_boat] -= 1
        else:
            return False
    for row_index in range(10):
        for column_index in range(10):
            if not field[row_index][column_index]:
                continue
            if (
                row_index != 0
                and not check_field(field, row_index + 1, column_index)
                and not check_field(field, row_index, column_index - 1)
                and not check_field(field, row_index, column_index + 1)
            ):
                boat_length_counter = 1
                following_square = field[row_index - boat_length_counter][column_index]
                while following_square:
                    field[row_index - boat_length_counter][column_index] = 0
                    boat_length_counter += 1
                    try:
                        following_square = field[row_index - boat_length_counter][
                            column_index
                        ]
                    except IndexError:
                        break
                field[row_index][column_index] = 0
                removed_boat = str(boat_length_counter)
                if removed_boat in boats.keys():
                    boats[removed_boat] -= 1
                else:
                    return False
            elif (
                column_index != 9
                and not check_field(field, row_index, column_index - 1)
                and not check_field(field, row_index - 1, column_index)
                and not check_field(field, row_index + 1, column_index)
            ):
                boat_length_counter = 1
                following_square = field[row_index][column_index + boat_length_counter]
                while following_square:
                    field[row_index][column_index + boat_length_counter] = 0
                    boat_length_counter += 1
                    try:
                        following_square = field[row_index][
                            column_index + boat_length_counter
                        ]
                    except IndexError:
                        break
                field[row_index][column_index] = 0
                removed_boat = str(boat_length_counter)
                if removed_boat in boats.keys():
                    boats[removed_boat] -= 1
                else:
                    return False
            elif (
                row_index != 9
                and not check_field(field, row_index - 1, column_index)
                and not check_field(field, row_index, column_index + 1)
                and not check_field(field, row_index, column_index - 1)
            ):
                boat_length_counter = 1
                following_square = field[row_index + boat_length_counter][column_index]
                while following_square:
                    field[row_index + boat_length_counter][column_index] = 0
                    boat_length_counter += 1
                    try:
                        following_square = field[row_index + boat_length_counter][
                            column_index
                        ]
                    except IndexError:
                        break
                field[row_index][column_index] = 0
                removed_boat = str(boat_length_counter)
                if removed_boat in boats.keys():
                    boats[removed_boat] -= 1
                else:
                    return False
            elif (
                column_index != 0
                and not check_field(field, row_index, column_index + 1)
                and not check_field(field, row_index + 1, column_index)
                and not check_field(field, row_index - 1, column_index)
            ):
                boat_length_counter = 1
                following_square = field[row_index][column_index - boat_length_counter]
                while following_square:
                    field[row_index][column_index - boat_length_counter] = 0
                    boat_length_counter += 1
                    try:
                        following_square = field[row_index][
                            column_index - boat_length_counter
                        ]
                    except IndexError:
                        break
                field[row_index][column_index] = 0
                removed_boat = str(boat_length_counter)
                if removed_boat in boats.keys():
                    boats[removed_boat] -= 1
                else:
                    return False
    if not bool(boats):
        return False
    return True
