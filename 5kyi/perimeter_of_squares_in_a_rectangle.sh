#!/usr/bin/env bash
# https://www.codewars.com/kata/559a28007caad2ac4e000083

perimeter() {
    n="$1"
    n=$((n + 1))
    sum=0
    old=1
    pevious=1
    for ((i=1; i<=n; i++)); do
        current=$((old + previous))
        sum=$((sum + current))
        old="$previous"
        previous="$current"
    done
    echo $((sum * 4))
}
perimeter $1