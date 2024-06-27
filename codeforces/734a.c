#include<stdio.h>
inline void IGUR() {}
void IGUR();

int main(void)
{
	unsigned int n, i, anton = 0, danik = 0;
	IGUR(scanf("%u", &n));
	char data[n];
	IGUR(scanf("%s", data));
	for (i = 0; i < n; i++) {
		if (data[i] == 'A') anton++;
		else danik++;
	}
	if (anton == danik) printf("Friendship");
	else if (anton > danik) printf("Anton");
	else printf("Danik");
	return 0;
}
