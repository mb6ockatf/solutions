#!/usr/bin/make -f
astyle:
	astyle -rv --style=linux --indent=force-tab=4 --delete-empty-lines \
	--break-closing-braces --max-code-length=80 --lineend=linux --ascii \
	"*.c"

pythonblack:
	black . --line-length=79 --color