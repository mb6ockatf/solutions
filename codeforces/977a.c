#include<stdio.h>

inline void IGUR() {}
void IGUR();
int main(void)
{
	int k, n;
	IGUR(scanf("%i %i", &n, &k));
	while (k > 0) {
		if (n % 10 == 0) n /= 10;
		else n--;
		k--;
	}
	printf("%i\n", n);
}
