#include <iostream>
#include <cstring>
#include <vector>
using namespace std;
int main()
{
    freopen("11054.txt", "r", stdin);
    int N;
    scanf("%d", &N);
    int A[N];
    for (int i = 0; i < N; i++)
    {
        scanf("%d ", &A[i]);
    }
    vector<int> DP(N);
    vector<int> PD(N);
    for (int i = 0; i < N; i++)
    {
        DP[i] = 1;
        for (int j = 0; j < i; j++)
        {
            if (A[j] < A[i] && DP[j] + 1 > DP[i])
            {
                DP[i] = DP[j] + 1;
            }
        }
    }
    for (int i = N - 1; i >= 0; i--)
    {
        PD[i] = 1;
        for (int j = N - 1; j > i; j--)
        {
            if (A[j] < A[i] && PD[j] + 1 > PD[i])
            {
                PD[i] = PD[j] + 1;
            }
        }
    }
    int result = 0;
    for (int i = 0; i < N; i++)
    {
        if (result < DP[i] + PD[i] - 1)
        {
            result = DP[i] + PD[i] - 1;
        }
    }
    printf("%d\n", result);
    return 0;
}