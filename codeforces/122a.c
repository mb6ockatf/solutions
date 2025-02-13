#include<stdio.h>
#include<stdbool.h>


int main(void)
{
	unsigned int value = 0;
	scanf("%u", &value);
	if (value % 4 == 0 || value % 7 == 0 || value % 47 == 0 || \
	                value % 74 == 0 || value % 477 == 0)
		{
			printf("YES\n");
			return 0;
		}
	printf("NO\n");
	return 0;
}
