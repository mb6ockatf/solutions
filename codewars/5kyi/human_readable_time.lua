#!/usr/bin/env lua
-- https://www.codewars.com/kata/52685f7382004e774f0001f7
local solution = {}
function solution.make_readable(seconds)
  local result
  local hours = math.floor(seconds / 3600)
  local minutes = math.floor(seconds / 60) % 60
  seconds = seconds % 60
  return string.format("%02d:%02d:%02d", hours, minutes, seconds)
end
return solution