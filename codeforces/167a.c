#include<stdio.h>
#include<string.h>
#include<math.h>
#include<limits.h>
#include<stdbool.h>
#include<stdlib.h>
#include<stdint.h>
#define GET_MACRO(_1,_2,_3,_4,NAME,...) NAME
#define FOR3(i,a,b) for(long long i=a;i<b;i++)
#define FOR4(i,a,b,step) for(long long i=a;i<b;i=i+step)
#define REV3(i,a,b) for(long long i=a;i>=b;i--)
#define REV4(i,a,b,step) for(long long i=a;i>=b;i=i-step)
#define FOR(...) GET_MACRO(__VA_ARGS__, FOR4, FOR3)(__VA_ARGS__)
#define REV(...) GET_MACRO(__VA_ARGS__, REV4, REV3)(__VA_ARGS__)
#define newl printf("\n");
#define t true
#define f false
#define b bool
#define d double
typedef unsigned int u;
typedef unsigned long lu;
typedef long long ll;
typedef unsigned long long llu;
inline void IGUR() {}
void IGUR();

b check_prime(int n)
{
	d limit = ceil(sqrt(n)) + 1;
	for (int i = 0; i < limit; i++) if (n % i == 0) return false;
	return true;
}

llu factorial(u n)
{
	llu result = 1;
	for (llu i = 1; i <= n; i++) result *= i;
	return result;
}

void proceed(void)
{
	int x, y;
	IGUR(scanf("%i %i", &x, &y));
	if (x > (50 - y) && y < 0) {
		printf("new NO\n");
		return;
	}
	if (y < 0 && abs(y) <= abs(x / 2)) {
		printf("YES\n");
		return;
	}
	if (y < 0) {
		printf("NO\n");
		return;
	}
	if (y > 0 && abs(x) < y) {
		printf("YES\n");
		return;
	}
	printf("YES\n");
}

int main(void)
{
	llu tests;
	IGUR(scanf("%llu", &tests));
	while (tests > 0) {
		proceed();
		tests--;
	}
}
