#include <iostream>
#include <cstring>
#include <vector>
using namespace std;

int N;
int main()
{
    freopen("13398.txt", "r", stdin);
    scanf("%d\n", &N);
    int A[N];
    for (int i = 0; i < N; i++)
    {
        scanf("%d ", &A[i]);
    }
    vector<int> DP(N);
    vector<int> PD(N);
    for (int i = 0; i < N; i++)
    {
        DP[i] = A[i];
        if (i == 0)
            continue;
        if (DP[i] < DP[i - 1] + A[i])
        {
            DP[i] = DP[i - 1] + A[i];
        }
    }
    for (int i = N - 1; i >= 0; i--)
    {
        PD[i] = A[i];
        if (i == N - 1)
            continue;
        if (PD[i] < PD[i + 1] + A[i])
        {
            PD[i] = PD[i + 1] + A[i];
        }
    }
    int result = DP[0];
    for (int i = 1; i < N; i++)
    {
        if (result < DP[i])
        {
            result = DP[i];
        }
    }
    for (int i = 1; i < N - 1; i++)
    {
        if (result < DP[i - 1] + PD[i + 1])
        {
            result = DP[i - 1] + PD[i + 1];
        }
    }
    printf("%d", result);
    return 0;
}