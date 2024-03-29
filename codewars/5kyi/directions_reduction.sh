#!/usr/bin/env bash
# https://www.codewars.com/kata/550f22f4d758534c1100025a

parameter=$1
changed=true
result=$parameter
while $changed; do
    parameter=$result
    if [ ${#parameter} -eq 1 ]; then
        break
    fi
    result=""
    changed=false
    for ((index=0; index <= ${#parameter}; index++)); do
        character="${parameter:index:1}"
        let next=$index+1
        nextchar="${parameter:next:1}"
        if [ "$index" -eq "${#parameter}" ]; then
            parameter+="$character"
            break
        fi
        if [ "$character" = "N" ]; then
            if [ "$nextchar" != "S" ]; then
                result+="N"
            else
                (( index++ ))
                changed=true
            fi
        elif [ "$character" = "S" ]; then
            if [ "$nextchar" != "N" ]; then
                result+="S"
            else
                (( index++ ))
                changed=true
            fi
        elif [ "$character" = "E" ]; then
            if [ "$nextchar" != "W" ]; then
                result+="E"
            else
                (( index++ ))
                changed=true
            fi
        elif [ "$character" = "W" ]; then
            if [ "$nextchar" != "E" ]; then
                result+="W"
            else
                (( index++ ))
                changed=true
            fi
        fi
        unset next
    done
done
echo "$parameter"
