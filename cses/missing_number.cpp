/*
Time limit: 1.00s Memory limit: 512 MB

You are given all numbers between 1, 2, ..., n except one. Your task is to find
the missing number.

# Input
The first input line contains an integer n.
The second line contains n-1 numbers. Each number is distinct and between 1 and
n (inclusive).

# Output
Print the missing number.
Constraints

2 <= n <= 2 * 10^5
---------------------------------- Example ------------------------------------
Input:
5
2 3 1 5

Output:
4
*/

#include <iostream>

using namespace std;

int main(void)
{
	unsigned long long n, sum, current, i;
	cin >> n;
	sum = (n + 1) * n / 2;
	for (i = 0; i < n - 1; i++) {
		cin >> current;
		sum -= current;
	}
	cout << sum;
}
