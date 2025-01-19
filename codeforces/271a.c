#include<stdio.h>
#include<stdint.h>
#include<stdlib.h>

int main(void)
{
	unsigned int y, attempt, a, b, c, d;
	if (scanf("%u", &y) != 1) {
		printf("no data was provided");
		return EXIT_FAILURE;
	}
	for (attempt = y + 1; attempt < y + 2000; attempt++) {
		a = attempt / 1000;
		b = (attempt - a * 1000) / 100;
		c = (attempt - a * 1000 - b * 100) / 10;
		d = (attempt - a * 1000 - b * 100 - c * 10);
		if (a != b && a != c && a != d && b != c && b != d && c != d) {
			break;
		}
	}
	printf("%u", attempt);
	return 0;
}
