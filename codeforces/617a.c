#include<stdio.h>
inline void IGUR() {}
void IGUR();

int main(void)
{
	unsigned int x, r = 0, i;
	IGUR(scanf("%u", &x));
	for (i = 5; i > 0; i--){
		r += x / i;
		x %= i;
	}
	printf("%u", r);
}
