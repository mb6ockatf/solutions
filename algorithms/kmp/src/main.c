#include <stdio.h>
#include <string.h>
#include <limits.h>

void preKmp(char *x, int x_length, int kmpNext[])
{
	int character_index = 0, offset = kmpNext[0] = -1;
	printf("%s\n", x);
	while (character_index < x_length) {
		for (int i=0; i < x_length; i++) {
			printf("%d ", kmpNext[i]);
		}
		printf("\n");
		printf("%d %d\n", offset, character_index);
		while (offset > -1 && x[character_index] != x[offset])
			offset = kmpNext[offset];
		character_index++;
		offset++;
		if (x[character_index] == x[offset])
			kmpNext[character_index] = kmpNext[offset];
		else
			kmpNext[character_index] = offset;
	}
}

void KMP(char *x, unsigned int x_length, char *y, int y_length)
{
	unsigned int i = 0, j = 0;
	int kmpNext[UINT_MAX];
	/* Preprocessing */
	preKmp(x, x_length, kmpNext);
	/* Searching */
	while (j < y_length) {
		while (i > -1 && x[i] != y[j]) i = kmpNext[i];
		i++;
		j++;
		if (i >= x_length) {
			printf("%i\n", j - i);
			i = kmpNext[i];
		}
	}
}
int main(void)
{
	int buffer[10000];
	preKmp("analanao", 8, buffer);
	return 0;
}
