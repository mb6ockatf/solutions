/*
Time limit: 1.00s Memory limit: 512 MB

A permutation of integers 1, 2, ..., n is called beautiful if there are no
adjacent elements whose difference is 1.
Given n, construct a beautiful permutation if such a permutation exists.

# Input
The only input line contains an integer n.
# Output
Print a beautiful permutation of integers 1, 2, ..., n. If there are several
solutions, you may print any of them. If there are no solutions, print "NO
SOLUTION".
Constraints

1 <= n <= 10^6

================================== Example 1 ==================================
Input:
5

Output:
4 2 5 3 1
================================== Example 2 ==================================
Input:
3

Output:
NO SOLUTION
*/

#include <iostream>
using namespace std;

int main(void)
{
	unsigned long long n, step;
	cin >> n;
	if (n == 2 || n == 3) {
		cout << "NO SOLUTION\n";
		return 0;
	}
	else if (n == 4) {
		cout << "2 4 1 3\n";
		return 0;
	}
	for (step = 0; step <= n / 2; step++) {
		if (n - step != n / 2) cout << n - step << " ";
		if (n / 2 - step != 0) cout << n / 2 - step << " ";
	}
}
