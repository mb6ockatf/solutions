#!/usr/bin/make -f
cc = gcc -std=c17
cc_optimization = -Ofast -march=native
#  -O3
cc_warnings = -Werror -Wall -Wextra -Wpedantic -Wshadow -Wconversion \
	      -pedantic -pedantic-errors -Wshadow \
	      -Wfloat-equal -Wlogical-op -Wshift-overflow=2 -Wduplicated-cond \
	      -Wcast-qual -Wcast-align -Wformat=2 \
	      -D_FORTIFY_SOURCE=2 -fsanitize=undefined -fno-sanitize-recover \
	      -fstack-protector -D_GLIBCXX_DEBUG -D_GLIBCXX_DEBUG_PEDANTIC \
	      -g
# -Wstrict-prototypes -Wold-style-definition
cc_link = -lgmp -lm

a: a.c
	${cc} ${cc_optimization} ${cc_warnings} $^ -o $@ ${cc_link}

b: b.c
	${cc} ${cc_optimization} ${cc_warnings} $^ -o $@ ${cc_link}

c: c.c
	${cc} ${cc_optimization} ${cc_warnings} $^ -o $@ ${cc_link}

d: d.c
	${cc} ${cc_optimization} ${cc_warnings} $^ -o $@ ${cc_link}

.PHONY: style

style:
	astyle -rv --style=linux --indent=force-tab=4 --delete-empty-lines \
	--break-closing-braces --max-code-length=80 --lineend=linux --ascii \
	"*.c"


clean:
	rm -rf main
