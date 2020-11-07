#include <iostream>
#include <cstring>
using namespace std;
// 11051
int triangle[1001][1001];
int mod = 10007;

int main()
{
    freopen("pascals_triangle.txt", "r", stdin);
    int N, K;
    scanf("%d %d", &N, &K);
    for (int n = 0; n <= N; n++)
    {
        triangle[n][0] = 1;
        for (int k = 1; k <= n - 1; k++)
        {
            triangle[n][k] = triangle[n - 1][k] + triangle[n - 1][k - 1];
            triangle[n][k] %= mod;
        }
        triangle[n][n] = 1;
    }
    printf("%d ", triangle[N][K]);
    return 0;
}