#!/usr/bin/make -f
cc = gcc -std=c23
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

.PHONY: style

style:
	astyle -r -A7 --indent=force-tab=4 --delete-empty-lines \
	--max-code-length=79 --lineend=linux -t8 "*.c"

main: main.c
	${cc} ${cc_optimization} ${cc_warnings} $^ -o $@ ${cc_link}

template: template.c
	${cc} ${cc_optimization} ${cc_warnings} $^ -o $@ ${cc_link}

t41a: 41a.c
	${cc} ${cc_optimization} ${cc_warnings} $^ -o $@ ${cc_link}

t59a: 59a.c  # реализация, строки, 800
	${cc} ${cc_optimization} ${cc_warnings} $^ -o $@ ${cc_link}

t110a: 110a.c  # реализация, 800
	${cc} ${cc_optimization} ${cc_warnings} $^ -o $@ ${cc_link}

t116a: 116a.c
	${cc} ${cc_optimization} ${cc_warnings} $^ -o $@ ${cc_link}

t734a: 734a.c  # реализация, строки, 800
	${cc} ${cc_optimization} ${cc_warnings} $^ -o $@ ${cc_link}

t1352a: 1352a.c  # реализация, математика, 800
	${cc} ${cc_optimization} ${cc_warnings} $^ -o $@ ${cc_link}

t791a: 791a.c  # реализация, 800
	${cc} ${cc_optimization} ${cc_warnings} $^ -o $@ ${cc_link}

t266a: 266a.c  # реализация, 800
	${cc} ${cc_optimization} ${cc_warnings} $^ -o $@ ${cc_link}

t546a: 546a.c  # математика, перебор, реализация, 800
	${cc} ${cc_optimization} ${cc_warnings} $^ -o $@ ${cc_link}

t617a: 617a.c  # математика, 800
	${cc} ${cc_optimization} ${cc_warnings} $^ -o $@ ${cc_link}

t977a: 977a.c  # реализация, 800
	${cc} ${cc_optimization} ${cc_warnings} $^ -o $@ ${cc_link}

t1873a: 1873a.c  # перебор, реализация, 800
	${cc} ${cc_optimization} ${cc_warnings} $^ -o $@ ${cc_link}

t1352b: 1352b.c  # конструктив, математика, 1200
	${cc} ${cc_optimization} ${cc_warnings} $^ -o $@ ${cc_link}

t1873b: 1873b.c  # жадные алгоритмы, математика, перебор, 800
	${cc} ${cc_optimization} ${cc_warnings} $^ -o $@ ${cc_link}

t1352c: 1352c.c  # бинарный поиск, математика, 1200
	${cc} ${cc_optimization} ${cc_warnings} $^ -o $@ ${cc_link}

t1873c: 1873c.c  # математика, реализация, 800
	${cc} ${cc_optimization} ${cc_warnings} $^ -o $@ ${cc_link}

t1873d: 1873d.c  # 2 указателя, жадные алгоритмы, реализация, 800
	${cc} ${cc_optimization} ${cc_warnings} $^ -o $@ ${cc_link}

t677a: 677a.c  # реализация, 800
	${cc} ${cc_optimization} ${cc_warnings} $^ -o $@ ${cc_link}

t271a: 271a.c  # перебор, 800
	${cc} ${cc_optimization} ${cc_warnings} $^ -o $@ ${cc_link}

t1030a: 1030a.c  # реализация, 800
	${cc} ${cc_optimization} ${cc_warnings} $^ -o $@ ${cc_link}

t58a: 58a.c  # жадные алгоритмы, строки, 1000
	${cc} ${cc_optimization} ${cc_warnings} $^ -o $@ ${cc_link}

t96a: 96a.c  # реализация, строки, 900
	${cc} ${cc_optimization} ${cc_warnings} $^ -o $@ ${cc_link}

t160a: 160a.c  # жадные алгоритмы, сортировки, 900
	${cc} ${cc_optimization} ${cc_warnings} $^ -o $@ ${cc_link}

clean:
	rm -rf main
	rm *.orig
