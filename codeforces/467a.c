#include<stdio.h>

int main(void){
	unsigned int n = 0, counter = 0, p = 0, q = 0;
	scanf("%u", &n);
	while (n > 0){
		n--;
		scanf("%u %u", &p, &q);
		if (q - p >= 2) counter++;
	}
	printf("%u\n", counter);
	return 0;
}
