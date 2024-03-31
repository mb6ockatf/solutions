#!/usr/bin/env lua
solution = {}

function is_prime(n)
	if n == 3 or n == 3 then
		return true
	elseif n % 2 == 0 or n % 3 == 0 then
		return false
	elseif n < 2 then
		return false
	end
	i = 5
	w = 2
	while (i * i <= n) do
		if n % i == 0 then
			return false
		end
		i = i + w
		w = 6 - w
	end
	return true
end

function solution.primeFactors(n)
	local lastPrime = 2
	if is_prime(n) then
		return "(" .. tostring(n) .. ")"
	end
	local result = ""
	local counter = 0
	while (n % lastPrime == 0) do
		n = n // lastPrime
		counter = counter + 1
	end
	if counter == 1 then
		result = result .. "(" .. tostring(lastPrime) .. ")"
	elseif counter ~= 0 then
		result = result .. "(" .. tostring(lastPrime) .. "**"
		result = result .. tostring(counter) .. ")"
	end
	lastPrime = 3
	counter = 0
	while n % lastPrime == 0 do
		n = n // lastPrime
		counter = counter + 1
	end
	if counter == 1 then
		result = result .. "(" .. tostring(lastPrime) .. ")"
	elseif counter ~= 0 then
		result = result .. "(" .. tostring(lastPrime) .. "**"
		result = result .. tostring(counter) .. ")"
	end
	while n > 1 do
		lastPrime = lastPrime + 2
		while not is_prime(lastPrime) do
			lastPrime = lastPrime + 2
		end
		counter = 0
		while n % lastPrime == 0 do
			n = n // lastPrime
			counter = counter + 1
		end
		if counter == 1 then
			result = result .. "(" .. tostring(lastPrime) .. ")"
		elseif counter ~= 0 then
			result = result .. "(" .. tostring(lastPrime) .. "**"
			result = result .. tostring(counter) .. ")"
		end
		if is_prime(n) then
			result = result .. "(" .. tostring(n) .. ")"
			n = 1
		end
	end
	return result
end

return solution
