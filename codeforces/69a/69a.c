#include<stdio.h>

int main(void)
{
	unsigned short int n = 0;
	short int x = 0, y = 0, z = 0, X = 0, Y = 0, Z = 0;
	scanf("%hu", &n);
	while (n > 0){
		n--;
		scanf("%hi %hi %hi", &x, &y, &z);
		X += x;
		Y += y;
		Z += z;
	}
	if (X == 0 && Y == 0 && Z == 0) printf("YES\n");
	else printf("NO\n");
	return 0;
}
