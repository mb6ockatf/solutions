#!/usr/bin/env lua
file = io.open("completed_tasks.ms", "r")
data = {}
for line in file:lines() do
	for element = 1, #data do
		if line == data[element] and line ~= ".NH" then
			io.write(line .. "\n")
		end
	end
	data[#data + 1] = line
end
