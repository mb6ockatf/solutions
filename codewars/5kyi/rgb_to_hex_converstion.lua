#!/usr/bin/env lua
-- https://www.codewars.com/kata/513e08acc600c94f01000001
local kata = {}
function kata.rgb(r, g, b)
	local result, args = "", {r, g, b}
	local first_sign
	for _, value in ipairs(args) do
		if value > 254 then
			result = result .. "FF"
		elseif value < 1 then
			result = result .. "00"
		else
			first_sign = string.format("%02x", value)
			result = result .. first_sign
		end
	end
	return result:upper()
end
return kata