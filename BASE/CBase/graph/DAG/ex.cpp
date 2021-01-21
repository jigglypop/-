#include <iostream>
#include <cstring>
using namespace std;
long long DP[201][201];
long long mod = 1000000000;
int main()
{
    freopen("2225.txt", "r", stdin);
    int N, K;
    scanf("%d %d", &N, &K);
    DP[0][0] = 1LL;
    for (int i = 1; i <= K; i++)
    {
        for (int j = 0; j <= N; j++)
        {
            for (int l = 0; l <= j; l++)
            {
                DP[i][j] += DP[i - 1][j - l];
                DP[i][j] %= mod;
            }
        }
    }
    printf("%d\n", DP[K][N]);
    return 0;
}