#include <iostream>
#include <cstdio>
using namespace std;
int N;
int A[1001];
int DP[1001];

int main()
{
    freopen("11055.txt", "r", stdin);
    scanf("%d", &N);
    for (int i = 0; i < N; i++)
    {
        scanf("%d", &A[i]);
    }
    for (int i = 0; i < N; i++)
    {
        DP[i] = A[i];
        for (int j = 0; j < i; j++)
        {
            if (A[i] > A[j] && DP[j] + A[i] > DP[i])
            {
                DP[i] = DP[j] + A[i];
            }
        }
    }
    int ans = 0;
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