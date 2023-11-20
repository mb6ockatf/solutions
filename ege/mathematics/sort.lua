#!/usr/bin/env lua
mfr = require("mfr")
data = {}
value = io.read()
while value ~= "!" do
	table.insert(data, tonumber(value))
	value = io.read()
end
table.sort(data)
-- mfr.pprint(data)
for i, name in ipairs(data) do
	io.write(name .. "\n")
end
