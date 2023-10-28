#!/usr/bin/env lua
-- https://www.codewars.com/kata/514b92a657cdc65150000006

local solution = {}

function solution.solution(value)
  local result = 0
  for c = value - 1, 1, -1 do
    if c % 3 == 0 then
      result = result + c
    elseif c % 5 == 0 then
      result = result + c
    end
  end
  return result
end

return solution