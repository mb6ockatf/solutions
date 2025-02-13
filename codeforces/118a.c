#include<stdio.h>
#include<stdbool.h>
#include<ctype.h>
#include<string.h>

bool isVowel(char letter)
{
	letter = (char)tolower(letter);
	switch (letter)
		{
		case 'a':
		case 'e':
		case 'i':
		case 'o':
		case 'u':
		case 'y':
			return true;
		}
	return false;
}

int main(void)
{
	char string[100], character;
	unsigned short int length = 0, i = 0;
	scanf("%s", string);
	length = (unsigned short int)strlen(string);
	for (i = 0; i < length; i++)
		{
			character = (char)tolower(string[i]);
			if (! isVowel(character))
				{
					printf(".%c", character);
				}
		}
	return 0;
}
