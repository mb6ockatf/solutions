#!/usr/bin/env bash
# https://www.codewars.com/kata/526571aae218b8ee490006f4
n=$(echo "obase=2;$1" | bc)
count=0
for ((i=0; i<${#n}; i++)); do
    if [ "${n:i:1}" == "1" ]; then
        count=$((count + 1))
    fi
done
echo $count