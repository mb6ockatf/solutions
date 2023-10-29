#!/usr/bin/env lua
-- https://www.codewars.com/kata/564057bc348c7200bd0000ff

local solution = {}

solution.row = {4, 3, 12, 9, 10, 1}

function solution.thirt(intNumber)
    local intCharacter, intShift, intAppendNumber
    local intResult, strNumber = 0, tostring(intNumber)
    local intLength = strNumber:len()
    local intMainShift = intLength % 6
    for index = strNumber:len(), 1, -1 do
      intCharacter = tonumber(strNumber:sub(index, index))
      intShift = math.abs((index + 6 - intMainShift) % 6)
      if intShift == 0 then intShift = 6 end
      intAppendNumber = intCharacter * solution.row[intShift]
      intResult = intResult + intAppendNumber
    end
    if intNumber == intResult then return intResult end
    return solution.thirt(intResult)
end

return solution