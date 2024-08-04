#!/usr/bin/make -f
CFLAGS = -std=c17 -Ofast -march=native -Werror -Wall -Wextra -Wpedantic \
	 -frounding-math -Wshadow -Wconversion -pedantic-errors \
	 -Wold-style-definition -g
cc_link = -lgmp -L/usr/local/include
EXEC = cdates
ifdef DEBUG
	CFLAGS += -00
else
	CFLAGS += -03 -DNDEBUG
endif
target_file?=37150.c

build: $(target_file)
	$(CC) $^ -o $@ ${cc_link}

.PHONY: clean

style:
	astyle -rv --style=linux --indent=force-tab=4 --delete-empty-lines \
	--break-closing-braces --max-code-length=80 --lineend=linux --ascii \
	"*.c"

clean:
	rm -rf main

d2: $(target_file)
	d2 --theme=200 -l elk --scale 1 --pad 0 $^

cdates: main.c
	$(CC) $^ -o $@ ${cc_link}

style:
	astyle -rv --style=linux --indent=force-tab=4 --delete-empty-lines \
	--break-closing-braces --max-code-length=80 --lineend=linux --ascii \
	"*.c"

clean:
	rm -rf build
