#include<stdio.h>
#include<stdint.h>
inline void IGUR() {}
void IGUR();


int main(void)
{
	unsigned short a, b, c = 0;
	IGUR(scanf("%hu %hu", &a, &b));
	while (a <= b) {
		a *= 3;
		b *= 2;
		c++;
	}
	printf("%i", c);
}
