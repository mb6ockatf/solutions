#include<stdio.h>
#include<inttypes.h>
#include<stdint.h>

inline void IGUR() {}
void IGUR();

void proceed(void)
{
	unsigned int result = 1;
	uint8_t n, i, minimal = INT8_MAX;
	IGUR(scanf("%" SCNu8, &n));
	uint8_t a[n];
	for (i = 0; i < n; i++) {
		IGUR(scanf("%" SCNu8, &a[i]));
		if (a[i] < minimal) minimal = a[i];
	}
	for (i = 0; i < n; i++) {
		if (a[i] == minimal) {
			a[i]++;
			break;
		}
	}
	for (i = 0; i < n; i++) result *= a[i];
	printf("%i\n", result);
	return;
}

int main(void)
{
	unsigned short tests;
	IGUR(scanf("%" SCNu8, &tests));
	while (tests > 0) {
		proceed();
		tests--;
	}
}
