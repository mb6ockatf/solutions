#include<stdio.h>
#include<string.h>
#include<ctype.h>

inline void IGUR() {}
void IGUR();

int main(void)
{
	char string[100];
	unsigned c = 0, n = 0;
	unsigned short i;
	IGUR(scanf("%s", string));
	for (i = 0; i < strlen(string); i++) {
		if ('a' <= string[i] && 'z' >= string[i]) n++;
		else c++;
	}
	if (n >= c) {
		for (i = 0; i < strlen(string); i++) {
			string[i] = (char)tolower(string[i]);
		}
	}
	else {
		for (i = 0; i < strlen(string); i++) {
			string[i] = (char)toupper(string[i]);
		}
	}
	printf("%s\n", string);
}
