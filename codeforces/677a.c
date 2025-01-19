#include<stdio.h>
#include<stdlib.h>
#include<stdint.h>
#include<errno.h>

int main(void)
{
	unsigned int n, h;
	if (scanf("%u %u", &n, &h) == EOF) {
		printf("no data was provided");
		return EXIT_FAILURE;
	}
	unsigned int * a = (unsigned int *)calloc(n, sizeof(unsigned int));
	if (a == NULL) {
		printf("memory allocation error");
		return ENOMEM;
	}
	for (unsigned int i = 0; i < n; i++) {
		if (scanf("%u", &a[i]) == EOF) {
			printf("no data was provided");
			return EXIT_FAILURE;
		}
	}
	unsigned int result = 0;
	for (unsigned int i = 0; i < n; i++) {
		if (a[i] > h) result += 2;
		else result += 1;
	}
	free(a);
	printf("%u", result);
	return 0;
}
