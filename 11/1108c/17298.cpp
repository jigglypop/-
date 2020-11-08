#include <cstring>
#include <iostream>
#include <stack>
#include <vector>
using namespace std;
int main()
{
    freopen("17298.txt", "r", stdin);
    int N;
    scanf("%d", &N);

    vector<int> A(N);
    vector<int> ans(N);
    for (int i = 0; i < N; i++)
    {
        scanf("%d ", &A[i]);
    }
    stack<int> S;
    S.push(0);
    for (int i = 0; i < N; i++)
    {
        if (S.empty())
            S.push(i);
        while (!S.empty() && A[S.top()] < A[i])
        {
            ans[S.top()] = A[i];
            S.pop();
        }
        S.push(i);
    }
    while (!S.empty())
    {
        ans[S.top()] = -1;
        S.pop();
    }
    for (int i = 0; i < N; i++)
        printf("%d ", ans[i]);
    return 0;
}