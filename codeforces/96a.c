#include<stdio.h>
#include<stdbool.h>
#include<stdint.h>

bool get_char(char * receiver)
{
	if (scanf("%s", receiver) != 1) return false;
	return true;
}

int finish(void)
{
	printf("YES");
	return 0;
}

int main(void)
{
	char situation[100], character;
	get_char(situation);
	bool checking_zeros = true;
	uint8_t i, counter = 0;
	for (i = 0; i < 100; i++) {
		character = situation[i];
		if (character == '0' && !checking_zeros) {
			checking_zeros = true;
			if (counter >= 7) return finish();
			counter = 1;
		}
		else if (character == '0' && checking_zeros) counter += 1;
		else if (character == '1' && checking_zeros) {
			checking_zeros = false;
			if (counter >= 7) return finish();
			counter = 1;
		}
		else if (character == '1' && ! checking_zeros) counter += 1;
		else if (character != '1' && character != '0') break;
	}
	if (counter >= 7) return finish();
	printf("NO");
	return 0;
}
