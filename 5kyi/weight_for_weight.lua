#!/usr/bin/env lua
-- https://www.codewars.com/kata/55c6126177c9441a570000cc

local solution = {}

function solution.orderWeight(str)
  if str == "" then
    return str
  end
  local result, value_weights = {}, {}
  local buffer
  for item in str:gmatch("%S*") do
    if item ~= "" and item ~= " " then
      buffer = 0
      for character_index = 1, #item do
        buffer = buffer + tonumber(item:sub(character_index, character_index))
      end
      table.insert(result, {tonumber(item), buffer})
    end
  end
  table.sort(result, function(a, b)
        if a[2] == b[2] then
          return tostring(a[1]) < tostring(b[1])
        end
        return a[2] < b[2]
      end)
  for key, value in ipairs(result) do
    result[key] = value[1]
  end
  return table.concat(result, " ")
end

return solution