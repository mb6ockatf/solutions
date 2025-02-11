#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int main(void)
{
	unsigned short n, r = 0;
	scanf("%hu", &n);
	char *s = (char *)malloc(n * sizeof(char));
	scanf("%s", s);
	for (int j = 1; j < n; j++)
		{
			if (s[j - 1] != s[j]) continue;
			r++;
		}
	free(s);
	printf("%hu", r);
}

