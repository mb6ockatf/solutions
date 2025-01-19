#include<stdio.h>
#include<stdlib.h>

int main(void)
{
	unsigned int x, r = 0, i;
	if (scanf("%u", &x) != 1) {
		printf("no data was provided");
		return EXIT_FAILURE;
	}
	for (i = 5; i > 0; i--) {
		r += x / i;
		x %= i;
	}
	printf("%u", r);
}
