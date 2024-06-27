#include<stdio.h>
inline void IGUR() {}
void IGUR();

int main(void)
{
	int k, n, w, r;
	IGUR(scanf("%i %i %i", &k, &n, &w));
	r = ((k + w * k) * w - 2 * n) / 2;
	printf("%i\n", (r > 0 ? r : 0));
}
