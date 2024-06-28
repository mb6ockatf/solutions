#include<stdio.h>
inline void IGUR() {}
void IGUR();

void proceed(void)
{
	char string[3];
	IGUR(scanf("%s", string));
	if (string[0] == 'a' || string[1] == 'b' || string[2] == 'c') {
		printf("YES\n");
		return;
	}
	printf("NO\n");
	return;
}

int main(void)
{
	unsigned short int tests;
	IGUR(scanf("%hu", &tests));
	while (tests > 0) {
		proceed();
		tests--;
	}
}
