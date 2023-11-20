/* https://inf-ege.sdamgia.ru/problem?id=37150 */
#include <stdio.h>
#include <stdbool.h>
int main(void)
{
	int a, x, y;
	bool fl;
	for(a=100; a>=0; a--) {
		fl = true;
		for (x = 0; x <= 100; x++)
			for (y = 0; y <= 100; y++)
				if (!((2 * x + y != 70) || (x < y) || (a < x)))
					fl = false;
		if (fl) {
			printf("%d", a);
			break;
		}
	}
}
