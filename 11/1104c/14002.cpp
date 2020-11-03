#include <iostream>
#include <cstring>
using namespace std;
int DP[1001];
int A[1001];
int V[1001];

void go(int i)
{
    if (i == -1)
    {
        return;
    }
    go(V[i]);
    printf("%d ", A[i]);
}

int main()
{
    freopen("14002.txt", "r", stdin);
    int N;
    scanf("%d", &N);
    for (int i = 0; i < N; i++)
    {
        scanf("%d", &A[i]);
    }
    for (int i = 0; i < N; i++)
    {
        DP[i] = 1;
        V[i] = -1;
        for (int j = 0; j < i; j++)
        {
            if (A[i] > A[j] && DP[j] + 1 > DP[i])
            {
                DP[i] = DP[j] + 1;
                V[i] = j;
            }
        }
    }
    int result = DP[0];
    int start = 0;
    for (int i = 0; i < N; i++)
    {
        if (DP[i] > result)
        {
            result = DP[i];
            start = i;
        }
    }
    printf("%d\n", result);
    go(start);
    return 0;
}