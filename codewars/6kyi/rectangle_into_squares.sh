#!/usr/bin/env bash
set -euo pipefail

sqInRect() {
	local width="$1"
	local length="$2"
	if [[ $width -eq $length ]]; then
		echo "nil"
		return 0
	fi
	result=""
	while [[ $width -ne 0 ]] && [[ $length -ne 0 ]]; do
		if [[ $width -gt $length ]]; then
			result="${result} $length"
			width=$((width - length))
		elif [[ $width -eq $length ]]; then
			result="${result} $width"
			break
		else
			result="${result} $width"
			length=$((length - width))
		fi
	done
	echo "$result" | sed 's/^[ \t]*//;s/[ \t]*$//'
}

sqInRect "$1" "$2"
