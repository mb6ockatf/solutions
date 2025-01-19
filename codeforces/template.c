#include<stdio.h>
#include<string.h>
#include<math.h>
#include<limits.h>
#include<ctype.h>
#include<inttypes.h>
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

bool get_uint8_t(uint8_t receiver)
{
	if (scanf("%hhu", &receiver) != 1) return false;
	return true;
}

bool get_signed_short_int(signed short int receiver)    // [-32767; +32767]
{
	if (scanf("%hd", &receiver) != 1) return false;
	return true;
}

bool get_unsigned_short_int(unsigned short int receiver)    // [0; 65535]
{
	if (scanf("%hu", &receiver) != 1) return false;
	return true;
}

bool get_signed_int(signed int receiver)   // [-32767; +32767]
{
	if (scanf("%i", &receiver) != 1) return false;
	return true;
}

bool get_unsigned_int(unsigned int receiver)   // [0; 65535]
{
	if (scanf("%u", &receiver) != 1) return false;
	return true;
}

// [-2 147 483 647; +2 147 483 647]
bool get_signed_long_int(signed long receiver)
{
	if (scanf("%ld", &receiver) != 1) return false;
	return true;
}

// [0; 4 294 967 295]
bool get_unsigned_long_int(unsigned long int receiver)
{
	if (scanf("%lu", &receiver) != 1) return false;
	return true;
}

// [-9 223 372 036 854 775 807; +9 223 372 036 854 775 807]
bool get_signed_long_long_int(signed long long int receiver)
{
	if (scanf("%lld", &receiver) != 1) return false;
	return true;
}

// [0; 18 446 744 073 709 551 615]
bool get_unsigned_long_long_int(unsigned long long int receiver)
{
	if (scanf("%llu", &receiver) != 1) return false;
	return true;
}

bool get_float(float receiver)   // 32 bits
{
	if (scanf("%f", &receiver) != 1) return false;
	return true;
}

bool get_double(double receiver)   // 64 bits
{
	if (scanf("%lf", &receiver) != 1) return false;
	return true;
}

bool get_long_double(long double receiver)   // 96 bits
{
	if (scanf("%Lf", &receiver) != 1) return false;
	return true;
}

bool get_char(char * receiver)
{
	if (scanf("%s", receiver) != 1) return false;
	return true;
}

bool check_prime(unsigned int n)
{
	double limit = ceil(sqrt(n)) + 1;
	for (unsigned int i = 2; i < limit; i++) if (n % i == 0) return false;
	return true;
}

unsigned long long factorial(unsigned int n)
{
	unsigned long long result = 1, i;
	for (i = 1; i <= n; i++) result *= i;
	return result;
}

void proceed(void)
{
	return;
}

int main(void)
{
	unsigned long long tests = 0;
	get_unsigned_long_long(tests);
	while (tests > 0) {
		proceed();
		tests--;
	}
}
