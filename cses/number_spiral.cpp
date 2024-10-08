/*
Time limit: 1.00s Memory limit: 512 MB

A number spiral is an infinite grid whose upper-left square has number 1. Here
are the first five layers of the spiral:
  1 |  2 |  9 | 10 | 25
----+----+----+----+---
  4 |  3 |  8 | 11 | 24
----+----+----+----+---
  5 |  6 |  7 | 12 | 23
----+----+----+----+---
 16 | 15 | 14 | 13 | 22
----+----+----+----+---
 17 | 18 | 19 | 20 | 21
Your task is to find out the number in row y and column x.

# Input
The first input line contains an integer t: the number of tests.
After this, there are t lines, each containing integers y and x.
# Output
For each test, print the number in row y and column x.
Constraints
1 <= t <= 10^5
1 <= y, x <= 10^9
---------------------------------- Example ------------------------------------
Input:
3
2 3
1 1
4 2
Output:
8
1
15
*/
#include <bits/stdc++.h>
using namespace std;
unsigned long long proceed(unsigned long long x, unsigned long long y)
{
	if (y <= x) {
		if (x % 2 == 0) return (x - 1) * (x - 1) + y;
		else return x * x - y + 1;
	}
	if (y % 2 == 0) return y * y - x + 1;
	else return (y - 1) * (y - 1) + x;
}

int main(void)
{
	unsigned long long tests, x, y;
	cin >> tests;
	while (tests != 0) {
		cin >> y;
		cin >> x;
		cout << proceed(x, y) << "\n";
		tests--;
	}
}
