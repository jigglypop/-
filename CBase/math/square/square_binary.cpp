#include <iostream>
#include <cstring>
using namespace std;
// 1629
long long calc(long long a, long long b, long long c)
{
    long long result = 1LL;
    while (b > 0)
    {
        if (b % 2 == 1)
        {
            result *= a;
            result %= c;
        }
        a = a * a;
        b /= 2;
        a %= c;
    }
    return result;
}

int main()
{
    freopen("square_divided.txt", "r", stdin);
    long long A, B, C;
    scanf("%lld %lld %lld", &A, &B, &C);
    printf("%lld", calc(A, B, C));
    return 0;
}