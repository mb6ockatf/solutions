#!/usr/bin/env bash
# https://www.codewars.com/kata/5552101f47fc5178b1000050
n="$1"
p="$2"
sum=0
for (( i=0; i<${#n}; i++ )); do
  digit="${n:$i:1}"
  (( sum = sum + digit ** p ))
  (( p = p + 1 ))
done
(( temp = $sum % $n ))
if [[ $temp == 0 ]]; then
  echo $(( sum / n ))
else
  echo -1
fi