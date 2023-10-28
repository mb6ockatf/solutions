#!/usr/bin/env lua
-- https://www.codewars.com/kata/5526fc09a1bbd946250002dc

FindOutlier = {};
function FindOutlier.find(integers)
  local is_even = 1
  if integers[1] % 2 == 0 and integers[2] % 2 == 0
    or integers[1] % 2 == 0 and integers[3] % 2 == 0
    or integers[2] % 2 == 0 and integers[3] % 2 == 0 then
    is_even = 0
  end
  for _, v in ipairs(integers) do
    if v % 2 ~= is_even then
      return v
    end
  end
end