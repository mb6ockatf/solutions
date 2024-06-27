#include<stdio.h>
inline void IGUR() {}
void IGUR();

void proceed(void)
{
	unsigned short int n, result[5], counter, r, shift;
	IGUR(scanf("%hu", &n));
	result[0] = counter = 0;
	shift = 1;
	while (n > 0) {
		r = n % 10;
		if (r != 0) {
			result[counter] = r * shift;
			counter++;
		}
		shift *= 10;
		n /= 10;
	}
	printf("%hu\n", counter);
	for (r = 0; r < counter; r++) printf("%hu ", result[r]);
	printf("\n");
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
