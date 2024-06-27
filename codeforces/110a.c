#include<stdio.h>
inline void IGUR() {}
void IGUR();

int main(void)
{
	long long n, r = 0, c = 0;
	IGUR(scanf("%lld", &n));
	while (n > 0) {
		r = n % 10;
		if (r == 4 || r == 7) c++;
		n /= 10;
	}
	if (c == 0) {
		printf("NO\n");
		return 0;
	}
	while (c > 0) {
		r = c % 10;
		if (r != 4 && r != 7) {
			printf("NO\n");
			return 0;
		}
		c /= 10;
	}
	printf("YES\n");
	return 0;
}
