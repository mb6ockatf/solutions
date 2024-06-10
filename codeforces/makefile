#!/usr/bin/make -f
cc = gcc
cc_standard = -std=c17
cc_optimization = -Ofast -march=native
cc_warnings = -Werror -Wall -Wextra -Wpedantic -Wshadow -Wconversion \
	-pedantic-errors -Wmissing-prototypes -Wmissing-prototypes \
	-Wstrict-prototypes -Wold-style-definition -O3 -g
cc_link = -lgmp

main: main.c
	${cc} ${cc_standard} ${cc_optimization} ${cc_warnings} $^ -o $@ ${cc_link}

.PHONY: main

style:
	astyle -rv --style=linux --indent=force-tab=4 --delete-empty-lines \
	--break-closing-braces --max-code-length=80 --lineend=linux --ascii \
	"*.c"


clean:
	rm -rf main
