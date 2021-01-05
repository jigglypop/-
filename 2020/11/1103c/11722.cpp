#include <iostream>
#include <cstdio>
using namespace std;
int N;
int A[1001];
int DP[1001];

int main()
{
    freopen("11722.txt", "r", stdin);
    scanf("%d", &N);
    for (int i = 0; i < N; i++)
    {
        scanf("%d", &A[i]);
    }
    for (int i = 0; i < N; i++)
    {
        DP[i] = 1;
        for (int j = 0; j < i; j++)
        {
            if (A[i] < A[j] && DP[j] + 1 > DP[i])
            {
                DP[i] = DP[j] + 1;
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