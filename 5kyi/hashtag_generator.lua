#!/usr/bin/env lua
-- https://www.codewars.com/kata/52449b062fb80683ec000024
local solution = {}

function solution.generate_hashtag(s)
  if s == "" then
    return false
  end
  local result = {}
  for item in s:gmatch("%S*") do
    value = item:lower():gsub("^%l", string.upper)
    table.insert(result, value)
  end
  result = "#" .. table.concat(result, "")
  if result:len() > 140 then
    return false
  end
  return result
end

return solution