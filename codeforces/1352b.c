#include<stdio.h>
inline void IGUR() {}
void IGUR();

void proceed(void)
{
	long n, r, k, j;
	IGUR(scanf("%li %li", &n, &k));
	r = n - k + 1;
	if (r % 2 != 0 && r > 0) {
		printf("yes\n");
		for (j = 0; j < k - 1; j++) printf("1 ");
		printf("%lu\n", r);
		return;
	}
	r = n - 2 * (k - 1);
	if (r % 2 == 0 && r > 0) {
		printf("yes\n");
		for (j = 0; j < k - 1; j++) printf("2 ");
		printf("%lu\n", r);
		return;
	}
	printf("no\n");
}

int main(void)
{
	unsigned short t;
	IGUR(scanf("%hu", &t));
	while (t > 0) {
		proceed();
		t--;
	}
}
