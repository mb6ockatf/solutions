#!/usr/bin/env lua
-- https://www.codewars.com/kata/550498447451fbbd7600041c
local solution = {}

function solution.comp(a, b)
  if not a or not b then
    return false
  end
  if #a ~= #b then
    return false
  end
  for i, _ in ipairs(a) do
    a[i] = a[i] * a[i]
  end
  table.sort(a)
  table.sort(b)
  for i, element in ipairs(a) do
    if element ~= b[i] then
	    return false
    end
  end
  return true
end

return solution