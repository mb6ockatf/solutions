dist_doc_DATA = README
bin_PROGRAMS = 467a

467a_SOURCES = 467a.c
AM_LDFLAGS = -lm
AM_CFLAGS = -std=c23 -Werror -Wall -Wextra -Wpedantic -Wshadow -Wconversion \
	   -pedantic-errors -Wfloat-equal -Wlogical-op -Wshift-overflow=2 \
	   -fsanitize=undefined -fno-sanitize-recover

clean-local:
	astyle --recursive --style=gnu --indent=force-tab=4 \
		--delete-empty-lines --max-code-length=80 --lineend=linux \
		--ascii -t8 "*.c"
	astyle --recursive --style=gnu --indent=force-tab=4 \
		--delete-empty-lines --max-code-length=80 --lineend=linux \
		--ascii -t8 "*.h"
	find . -name '*.orig' -exec rm -f {} +
