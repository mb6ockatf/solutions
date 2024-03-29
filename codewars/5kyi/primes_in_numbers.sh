#!/usr/bin/env bash

isPrime(){
    if [[ $1 -eq 2 ]] || [[ $1 -eq 3 ]]; then
		echo true
		return 0
	elif [[ $(($1 % 2)) -eq 0 ]] || [[ $(($1 % 3)) -eq 0 ]]; then
		echo false
		return 0
    fi
    i=5
	w=2
    while [[ $((i * i)) -le $1 ]]; do
        if [[ $(($1 % i)) -eq 0 ]]; then
			echo false
			return 0
        fi
        i=$((i + w))
		w=$((6 - w))
    done
	echo true
}

# echo -n "nextPrime 1 : "
# echo $(nextPrime 1)
# echo -n "nextPrime 2 : "
# echo $(nextPrime 2)
primeFactors() {
	local lastPrime=1
	local number="$1"
	if "$(isPrime "$number")"; then
		echo "($number)"
		return 0
	fi
	local result=""; local counter
	while (( number > 1 )); do
		lastPrime=$((lastPrime + 1))
		while ! $(isPrime $lastPrime); do
			lastPrime=$((lastPrime + 1))
		done
		counter=0
		while (( number % lastPrime == 0 )); do
			number=$((number / lastPrime))
			counter=$((counter + 1))
		done
		if [[ $counter -eq 1 ]]; then
			result="${result}($lastPrime)"
		elif [[ $counter -ne 0 ]]; then
			result="${result}($lastPrime**$counter)"
		fi
		if $(isPrime "$number"); then
			result="${result}($number)"
			number=1
		fi
	done
	echo "$result"
}
# primeFactors $1
# echo "aboba"
primeFactors 9
# primeFactors 26112091316332
echo -n "$(primeFactors 365400012)"
echo "              | (36540001)"
# echo "anadeba"
echo -n "$(primeFactors 86240)"
echo "                | (2**5)(5)(7**2)(11)"
echo -n "$(primeFactors 7775460)"
echo "      | (2**2)(3**3)(5)(7)(11**2)(17)"
echo -n "$(primeFactors 7919)"
echo "                             | 7919"
echo -n "$(primeFactors $(( 17 * 17 * 93 * 677 )))"
echo "                | (3)(17**2)(31)(677)"
echo -n "$(primeFactors 342217392)"
echo "           | (2**4)(3)(11)(43)(15073)"
for i in $(seq 200); do
	primeFactors "$(shuf -i 63235-3548569 -n 1)" &>/dev/null
done
