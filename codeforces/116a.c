#include<stdio.h>
#include<limits.h>
inline void IGUR() {}
void IGUR();

int main(void)
{
	unsigned short a, b, n;
	int current = 0;
	int result = INT_MIN;
	IGUR(scanf("%hu", &n));
	while (n > 0) {
		IGUR(scanf("%hu %hu", &a, &b));
		current = current - a + b;
		if (current > result) result = current;
		n--;
	}
	printf("%i\n", result);
	return 0;
}
