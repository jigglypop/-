#include <iostream>
#include <cstring>
using namespace std;
int DP[100001][3];

int main()
{
    freopen("1309.txt", "r", stdin);
    int N;
    scanf("%d", &N);
    DP[0][0] = 1;
    for (int i = 1; i <= N; i++)
    {
        DP[i][0] = DP[i - 1][0] + DP[i - 1][1] + DP[i - 1][2];
        DP[i][1] = DP[i - 1][0] + DP[i - 1][2];
        DP[i][2] = DP[i - 1][0] + DP[i - 1][1];
        for (int j = 0; j < 3; j++)
        {
            DP[i][j] %= 9901;
        }
    }
    printf("%d\n", (DP[N][0] + DP[N][1] + DP[N][2]) % 9901);
    return 0;
}