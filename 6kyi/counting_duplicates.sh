#!/usr/bin/env bash
# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1
echo $1 | grep -o . | sort -f | uniq -id | wc -l