#!/usr/bin/env bash
# https://www.codewars.com/kata/559a28007caad2ac4e000083
perimeter() {
    arg=$(("$1" - 1))
    result=2
    previous=1
	current=1
	next=0
	for i in $(seq $arg); do
		next=$(($previous + $current))
		result=$(($result + $next))
		previous=$current
		current=$next
    done
	echo $((4 * $result))
}

perimeter $1

