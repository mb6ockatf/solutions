/* https://inf-ege.sdamgia.ru/problem?id=38589 
 * BROKEN
 */
#include <stdio.h>
#include <math.h>
#include <string.h>
__extension__ typedef __int128 int128;
const unsigned long long int PRECISION = 10ULL;
unsigned __int128 ipow(unsigned __int128 base, unsigned __int128 exp);
unsigned __int128 ipow(unsigned __int128 base, unsigned __int128 exp)
{
    unsigned __int128 result = 1ULL;
    while( exp )
    {
        if ( exp & 1 )
        {
            result *= (unsigned __int128)base;
        }
        exp >>= 1;
        base *= base;
    }
    return result;
}
int main(void) {
	unsigned __int128 number1, number2, number3, number4, number5, sum;
	number1 = ipow(4ULL, 38ULL);
	number2 = 2ULL * ipow(4ULL, 23ULL);
	number3 = ipow(4ULL, 20ULL);
	number4 = 3ULL * ipow(4ULL, 5ULL);
	number5 = 2ULL * ipow(4ULL, 4ULL) + 1ULL;
	sum = 3ULL * number1 + number2 + number3 + number4 + number5;
	printf("%ll", value);
	printf("%ll\n", sum);
	unsigned char string[400] = "";
	unsigned short int i = 0, count = 0;
	while (sum) {
		string[i] = (sum % 16) + '0';
		sum /= 16ULL;
		i++;
	}
	for (int j = 0; string[j] != '\0'; j++) {
		if (string[j] == '0')
			count++;
	}
	unsigned long long int part1, part2;
	part2 = count % PRECISION;
	part1 = count / PRECISION;
	printf("%llu", part1);
	printf("%llu", part2);
	return 0;
}
