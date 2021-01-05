#include <iostream>
#include <cstring>
using namespace std;
// 1629
long long calc(long long a, long long b, long long c)
{
    if (b == 0)
        return 1LL;
    else if (b == 1)
        return a % c;
    else if (b % 2 == 1)
        return (a * calc(a, b - 1, c)) % c;
    else
    {
        // 최적화 주의
        long long temp = calc(a, b / 2, c);
        return (temp * temp) % c;
    }
}

int main()
{
    freopen("square_divided.txt", "r", stdin);
    long long A, B, C;
    scanf("%lld %lld %lld", &A, &B, &C);
    printf("%lld", calc(A, B, C));
    return 0;
}