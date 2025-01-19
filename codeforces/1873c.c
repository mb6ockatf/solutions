#include<stdio.h>
#include<stdint.h>
inline void IGUR() {}
void IGUR();

uint8_t get_points(char* string, uint8_t row)
{
	uint8_t i, column, result = 0;
	for (i = 0; i < 10; i++) {
		if (string[i] != 'X') continue;
		column = i + 1;
		if (row == 1 || row == 10 || column == 1 || column == 10) {
			result += 1;
		}
		if (((row == 2 || row == 9) && 1 < column && column < 10)
		    || ((column == 2
		         || column == 9) && 1 < row && row < 10)) {
			result += 2;
		}
		if (((row == 3 || row == 8) && 2 < column && column < 9)
		    || ((column == 3
		         || column == 8) && 2 < row && row < 9)) {
			result += 3;
		}
		if (((row == 4 || row == 7) && 3 < column && column < 8)
		    || ((column == 4
		         || column == 7) && 3 < row && row < 8)) {
			result += 4;
		}
		if (((row == 5 || row == 6) && 4 < column && column < 7)
		    || ((column == 5
		         || column == 6) && 4 < row && row < 7)) {
			result += 5;
		}
	}
	return result;
}

int main(void)
{
	unsigned short tests;
	IGUR(scanf("%hu", &tests));
	while (tests > 0) {
		uint8_t i, result = 0;
		char buffer[10];
		for (i = 0; i < 10; i++) {
			IGUR(scanf("%s", buffer));
			result += get_points(buffer, i + 1);
		}
		printf("%hhu\n", result);
		tests--;
	}
}
