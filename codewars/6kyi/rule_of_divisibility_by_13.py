#!/usr/bin/env python3
# https://www.codewars.com/kata/564057bc348c7200bd0000ff

row = [4, 3, 12, 9, 10, 1]


def thirt(intNumber: int) -> int:
    intResult, strNumber = 0, str(intNumber)
    intLength = len(strNumber)
    intMainShift = intLength % 6
    for index in range(intLength, 0, -1):
        intCharacter = int(strNumber[index - 1])
        intShift = (index + 5 - intMainShift) % 6
        print(intCharacter, row[intShift])
        intResult += intCharacter * row[intShift]
    if intNumber == intResult:
        return intResult
    return thirt(intResult)
