#include<stdio.h>
#include<string.h>

int main(void)
{
	char nickname[100];
	short buffer = 0;
	short distinct = 0;
	scanf("%[^\n]s", nickname);
	for (short i = 0; i < (short)strlen(nickname); i++) {
		buffer = 0;
		for (short k = 0; k < i; k++) {
			(void)((nickname[k] == nickname[i]) && buffer++);
			if (buffer > 0) break;
		}
		if (buffer == 0) distinct++;
	}
	if (distinct % 2 == 0) printf("CHAT WITH HER!\n");
	else printf("IGNORE HIM!\n");
	return 0;
}
