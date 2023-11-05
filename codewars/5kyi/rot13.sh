#!/usr/bin/env bash
# https://www.codewars.com/kata/530e15517bc88ac656000716
echo "$(echo $1 | tr '[A-Z]' '[N-ZA-M]' | tr '[a-z]' '[n-za-m]')"