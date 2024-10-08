#!/usr/bin/make -f
CFLAGS = -Ofast -march=native -Werror -Wall -Wextra -Wpedantic -Wshadow \
	 -Wconversion -pedantic-errors -O3 -g -lgmp

style:
	astyle -rvA8T8xeyxC70z2xWYK "*.cpp"
	astyle -rvA8T8xeyxC70z2xWYK "*.h"
	find . -name '*.orig' -exec rm -f {} +

clean:
	rm -f $(OBJ) build orig
