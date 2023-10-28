#!/usr/bin/env lua
-- https://www.codewars.com/kata/58f5c63f1e26ecda7e000029
local solution = {}

function solution.wave(str)
  local temp = {}
  local result = {}
  for i = 1, str:len() do
    if str:sub(i, i) ~= " " then
      for i = 1, str:len() do
        table.insert(temp, str:sub(i, i))
      end
      temp[i] = temp[i]:upper()
      temp = table.concat(temp, "")
      table.insert(result, temp)
      temp = {}
    end
  end
  return result
end

return solution