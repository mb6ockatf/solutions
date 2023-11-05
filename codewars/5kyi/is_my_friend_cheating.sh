#!/usr/bin/env bash
# https://www.codewars.com/kata/5547cc7dcad755e480000004

n="$1"
comma_printed=true
((sum = (n + 1) * n / 2))

function print_needed_comma() {
	if [[ $1 = false ]]; then
		printf ","
	fi
}

for (( a = 1; a <= n; a++ )); do
	b=$((($sum - $a) % ($a + 1)))
	if ((b == 0)); then
		b=$((($sum - $a) / ($a + 1)))
		if (( $b <= $n )); then
			print_needed_comma $comma_printed
			printf "$a $b"
			comma_printed=false
		fi
	fi
done