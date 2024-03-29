#!/usr/bin/env bash

repeat_char() { for ((i = 1; i < $2; i++)); do echo -n "$1"; done }

# set -euo pipefail
s1=`echo "$1" | grep -o . | sort | tr -d "\n"`  # read -r s1
s2=`echo "$2" | grep -o . | sort | tr -d "\n"`  # read -r s2
first=true
alphabet="abcdefghijklmnopqrstuvwxyz"
for (( i=0; i<${#alphabet}; i++ )); do
	character="${alphabet:$i:1}"
	if ! [[ "$character" =~ [a-z] ]]; then continue; fi
	occurences_s1=`grep -o "$character" <<< "$s1" | grep -c .`
	occurences_s2=`grep -o "$character" <<< "$s2" | grep -c .`
	if (( $occurences_s1 <= 1 )) && (( occurences_s2 <= 1 )); then continue; fi
	if ! $first; then
		echo -n "/"
	else
		first=false
	fi
	if (( $occurences_s1 > $occurences_s2 )); then
		echo -n "1:"`repeat_char $character $occurences_s1`
	elif (( $occurences_s2 > $occurences_s1 )); then
		echo -n "2:"`repeat_char $character $occurences_s2`
	elif [[ $occurences_s1 -eq $occurences_s2 ]]; then
		echo -n "=:"`repeat_char $character $occurences_s1`
	fi
done

