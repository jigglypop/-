#include <iostream>
#include <cstdio>
using namespace std;
long long DP[1000001];
const long long mod = 1000000009LL;
int main()
{
    freopen("15988.txt", "r", stdin);
    DP[0] = 1;
    for (int i = 1; i <= 1000000; i++)
    {
        if (i - 1 >= 0)
        {
            DP[i] += DP[i - 1];
        }
        if (i - 2 >= 0)
        {
            DP[i] += DP[i - 2];
        }
        if (i - 3 >= 0)
        {
            DP[i] += DP[i - 3];
        }
        DP[i] %= mod;
    }
    int T;
    scanf("%d", &T);
    while (T--)
    {
        int N;
        scanf("%d", &N);
        printf("%d\n", DP[N]);
    }
}