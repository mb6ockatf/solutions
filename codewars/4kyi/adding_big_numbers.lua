#!/usr/bin/env lua
-- https://www.codewars.com/kata/525f4206b73515bffb000b21
local solution = {}

function solution.add(a, b)
	local strResult, intPlusser = "", 0
  if a == nil or a == "" then return b:match("0*(%d+)") end
	if b == nil or b == "" then return a:match("0*(%d+)") end
	a = a:match("0*(%d+)")
	b = b:match("0*(%d+)")
	local intALength, intBLength = string.len(a), string.len(b)
	a = a:reverse() .. string.rep("0", intBLength - intALength)
	b = b:reverse() .. string.rep("0", intALength - intBLength)
	local intLength = a:len()
	local strSummer, intSymbolA, intSymbolB
	for i = 1, intLength do
		intSymbolA = tonumber(a:sub(i, i)) or 0
		intSymbolB = tonumber(b:sub(i, i)) or 0
		strSummer = tostring(intSymbolA + intSymbolB + intPlusser)
		intPlusser = 0
		if strSummer:len() == 2 then
			intPlusser = tonumber(strSummer:sub(1, 1)) or 0
			strResult = strSummer:sub(2, 2) .. strResult
		else strResult = strSummer .. strResult end
	end
	if intPlusser ~= 0 then
    strResult =	tostring(intPlusser) .. strResult
  end
	return strResult
end

return solution