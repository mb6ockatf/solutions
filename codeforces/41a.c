#include<stdio.h>
#include<string.h>

inline void IGUR() {}
void IGUR();

int main(void)
{
	char s[1000];
	IGUR(scanf("%[^\n]s", s));
	unsigned short length = 0, i = 0;
	length = (unsigned short int)strlen(s);
	char t[1000];
	IGUR(scanf("%s", t));
	if (strlen(s) != strlen(t)) {
		printf("NO\n");
		return 0;
	}
	for (i = 0; i < length; i++) {
		if (s[i] != t[length - i - 1]) {
			printf("NO\n");
			return 0;
		}
	}
	printf("YES\n");
	return 0;
}
