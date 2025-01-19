#include<stdio.h>
#include<stdlib.h>
#include<stdint.h>

int compare(const void * a, const void * b)
{
	return - (*(const unsigned short int *)a - *(const unsigned short int *)b);
}

int main(void)
{
	unsigned short int n = 0, a = 0, i = 0, sum = 0;
	if (scanf("%hu", &n) != 1) {
		printf("no data provided");
		return EXIT_FAILURE;
	}
	unsigned short int list[n];
	for (i = 0; i < n; i++) {
		if (scanf("%hu", &list[i]) != 1) {
			printf("\nno data provided\n");
			return EXIT_FAILURE;
		}
		sum += list[i];
	}
	size_t element_size = sizeof(list) / sizeof(list[0]);
	qsort(list, element_size, sizeof(unsigned short), compare);
	i = 0;
	while (a <= sum) {
		a += list[i];
		sum -= list[i];
		i += 1;
	}
	printf("%hu", i);
	return 0;
}
