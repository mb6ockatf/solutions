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
	return;
}

int main(void)
{
	llu t;
	IGUR(scanf("%llu", t));
	while (t > 0) {
		proceed();
		t--;
	}
}
