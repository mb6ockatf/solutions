#!/usr/bin/env lua
local solution = {}

function solution.race(v1, v2, g)
	if v1 >= v2 then
		return {-1, -1, -1}
	end
	local growth = v2 - v1;
	local hours = g // growth;
	g = (g - hours * growth) * 60
	local minutes = g // growth
	g = (g - minutes * growth) * 60
	local seconds = g // growth
	return {hours, minutes, seconds}
end

return solution

