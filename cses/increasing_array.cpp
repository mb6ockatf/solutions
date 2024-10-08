/*
Time limit: 1.00s Memory limit: 512 MB

You are given an array of n integers. You want to modify the array so that it
is increasing, i.e., every element is at least as large as the previous
element.
On each move, you may increase the value of any element by one. What is the
minimum number of moves required?

# Input
The first input line contains an integer n: the size of the array.
Then, the second line contains n integers x1, x2, ..., x_n: the contents of
the array.

# Output
Print the minimum number of moves.
Constraints

1 <= n <= 2 * 10^5
1 <= x_i <= 10^9

---------------------------------- Example ------------------------------------
Input:
5
3 2 5 1 7

Output:
5
*/

#include <iostream>
using namespace std;

int main(void)
{
	unsigned long long n, current, last, moves = 0;
	cin >> n;
	cin >> last;
	while (n > 1) {
		cin >> current;
		if (current < last) moves += last - current;
		else last = current;
		n--;
	}
	cout << moves;
}
