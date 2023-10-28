#!/usr/bin/env lua
-- https://www.codewars.com/kata/5264d2b162488dc400000001
local solution = {}

function solution.split(str)
    local result, temp = {}, ""
    local character
    for index = 1, str:len() do
        character = str:sub(index, index)
        if character == " " then
            result[#result + 1] = temp
            temp = ""
        else
            temp = temp .. character
        end
    end
    result[#result + 1] = temp
    return result
end

function solution.spin_words(sentence)
    local result = {}
    sentence = solution.split(sentence)
    for _, value in ipairs(sentence) do
        if value:len() > 4 then value = value:reverse() end
        result[#result + 1] = value
    end
    return table.concat(result, " ")
end

return solution