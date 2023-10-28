#!/usr/bin/env bash
# https://www.codewars.com/kata/52685f7382004e774f0001f7

total_seconds=$1
hours=$((total_seconds / (60 * 60)))
minutes=$(((total_seconds / 60) % 60))
seconds=$((total_seconds % 60))
printf "%02d:%02d:%02d" $hours $minutes $seconds