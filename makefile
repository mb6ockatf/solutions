#!/usr/bin/make -f
astyle:
	astyle -rvA8T8xeyxC70z2xWYK "*.c"
	# astyle -rvA8T8xeyxC70z2xWYK "*.h"
	find . -name '*.orig' -exec rm -f {} +

pythonblack:
	black . --line-length=79 --color
