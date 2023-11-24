#!/usr/bin/make -f
cc = gcc
cc_standard = -std=c17
cc_optimization = -Ofast -march=native
cc_warnings = -Werror -Wall -Wextra -Wpedantic -frounding-math \
	-pedantic-errors -Wshadow -Wconversion -Wmissing-prototypes\
	-Wmissing-prototypes -Wstrict-prototypes \
	-Wold-style-definition -O3 -g
cc_link = -lgmp

target_file?=37150.c

build: $(target_file)
	${cc} ${cc_standard} ${cc_optimization} ${cc_warnings} $^ -o $@ ${cc_link}

.PHONY: clean

style:
	astyle -rv --style=linux --indent=force-tab=4 --delete-empty-lines \
	--break-closing-braces --max-code-length=80 --lineend=linux --ascii \
	"*.c"

clean:
	rm -rf main

docs:
	groff -ms *.ms -T pdf > completed_tasks.pdf
