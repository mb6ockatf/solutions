#include<stdio.h>
#include<string.h>
inline void IGUR() {}
void IGUR();

int main(void)
{
	unsigned short n, r = 0;
	IGUR(scanf("%hu", &n));
	char s[n];
	IGUR(scanf("%s", s));
	for (int j = 1; j < n; j++){
		if (s[j - 1] != s[j]) continue;
		r++;
	}
	printf("%hu", r);
}
