/*
You are given a DNA sequence: a string consisting of characters A, C, G, and T.
Your task is to find the longest repetition in the sequence. This is a
maximum-length substring containing only one type of character.

# Input
The only input line contains a string of n characters.

# Output
Print one integer: the length of the longest repetition.
Constraints

1 <= n <= 10^6

---------------------------------- Example ------------------------------------
Input:
ATTCGGGA

Output:
3
*/
#include <iostream>

using namespace std;

int main(void)
{
	unsigned long long counter = 0, maximal = 0;
	char previous = '0';
	char c;
	while (cin.get(c)) {
		if (c == previous) counter++;
		else {
			if (counter > maximal) maximal = counter;
			previous = c;
			counter = 1;
		}
	}
	cout << maximal;
}
