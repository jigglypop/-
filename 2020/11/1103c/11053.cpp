#include <iostream>
#include <cstring>

using namespace std;
int DP[1001];
int A[1001];
int main()
{
    freopen("11053.txt", "r", stdin);
    int N;
    scanf("%d", &N);
    for (int i = 0; i < N; i++)
    {
        scanf("%d", &A[i]);
    }
    for (int j = 0; j < N; j++)
    {
        DP[j] = 1;
        for (int i = 0; i < j; i++)
        {
            if (A[j] > A[i])
            {
                DP[j] = max(DP[i] + 1, DP[j]);
            }
        }
    }
    int ans = DP[0];
    for (int i = 0; i < N; i++)
    {
        if (ans < DP[i])
        {
            ans = DP[i];
        }
    }
    printf("%d\n", ans);
    return 0;
}