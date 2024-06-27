#include<stdio.h>
inline void IGUR() {}
void IGUR();

void proceed(void)
{
	unsigned long n, k;
	IGUR(scanf("%lu %lu", &n, &k));
	printf("%lu\n", k + (k - 1) / (n - 1));
}

int main(void)
{
	unsigned short int t;
	IGUR(scanf("%hu", &t));
	while (t > 0) {
		proceed();
		t--;
	}
}
