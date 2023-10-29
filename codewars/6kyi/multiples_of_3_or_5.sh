#!/usr/bin/env bash
# https://www.codewars.com/kata/514b92a657cdc65150000006

sum=0
n=$(($1 - 1))
for number in $(seq $n); do
    if [[ $(($number % 3)) -eq 0 ]] || [[ $((number % 5)) -eq 0 ]]; then
        sum=$((sum + number))
    fi
done
echo $sum