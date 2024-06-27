#!/usr/bin/make -f
cc = gcc
cc_standard = -std=c17
cc_optimization = -Ofast -march=native
cc_warnings = -Werror -Wall -Wextra -Wpedantic -Wshadow -Wconversion \
	      -pedantic -pedantic-errors -Wshadow \
	      -Wfloat-equal -Wlogical-op -Wshift-overflow=2 -Wduplicated-cond \
	      -Wcast-qual -Wcast-align -Wformat=2 \
	      -D_FORTIFY_SOURCE=2 -fsanitize=undefined -fno-sanitize-recover \
	      -fstack-protector -D_GLIBCXX_DEBUG -D_GLIBCXX_DEBUG_PEDANTIC \
	      -O3 -g
# -Wstrict-prototypes -Wold-style-definition
cc_link = -lgmp -lm

main: main.c
	${cc} ${cc_standard} ${cc_optimization} ${cc_warnings} $^ -o $@ \
		${cc_link}

template: template.c
	${cc} ${cc_standard} ${math_libs} ${cc_optimization} ${cc_warnings} \
		$^ -o $@ ${cc_link}

t1352a: 1352a.c
	${cc} ${cc_standard} ${cc_optimization} ${cc_warnings} $^ -o $@ \
		${cc_link}

t1352b: 1352b.c
	${cc} ${cc_standard} ${cc_optimization} ${cc_warnings} $^ -o $@ \
		${cc_link}

t1352c: 1352c.c
	${cc} ${cc_standard} ${cc_optimization} ${cc_warnings} $^ -o $@ \
		${cc_link}

t791a: 791a.c
	${cc} ${cc_standard} ${cc_optimization} ${cc_warnings} $^ -o $@ \
		${cc_link}

t266a: 266a.c
	${cc} ${cc_standard} ${cc_optimization} ${cc_warnings} $^ -o $@ \
		${cc_link}

t617a: 617a.c
	${cc} ${cc_standard} ${cc_optimization} ${cc_warnings} $^ -o $@ \
		${cc_link}

.PHONY: main

style:
	astyle -rv --style=linux --indent=force-tab=4 --delete-empty-lines \
	--break-closing-braces --max-code-length=80 --lineend=linux --ascii \
	"*.c"


clean:
	rm -rf main
