#include<stdio.h>
#include<stdint.h>
#include<stdlib.h>

int main(void)
{
	uint8_t n;
	uint8_t opinion;
	if (scanf("%hhu", &n) != 1) {
		printf("no data was provided");
		return EXIT_FAILURE;
	}
	for (uint8_t i = 0; i < n; i++) {
		if (scanf("%hhu", &opinion) != 1) {
			printf("no data was provided");
			return EXIT_FAILURE;
		}
		if (opinion == 1) {
			printf("hArD");
			return 0;
		}
	}
	printf("eAsY");
	return 0;
}
