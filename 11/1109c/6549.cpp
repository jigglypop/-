#include <cstring>
#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <algorithm>
using namespace std;
long long A[100000];

int main()
{
    freopen("6549.txt", "r", stdin);
    while (true)
    {
        int n;
        scanf("%d", &n);
        if (n == 0)
            break;
        for (int i = 0; i < n; i++)
            scanf("%lld", &A[i]);
        stack<long long> S;
        long long ans = 0;
        for (int i = 0; i < n; i++)
        {
            while (!S.empty() && A[S.top()] > A[i])
            {
                long long height = A[S.top()];
                S.pop();
                long long width = i;
                if (!S.empty())
                    width = (i - S.top() - 1);
                ans = max(width * height, ans);
            }
            S.push(i);
        }
        while (!S.empty())
        {
            long long height = A[S.top()];
            S.pop();
            long long width = n;
            if (!S.empty())
                width = n - S.top() - 1;
            ans = max(width * height, ans);
        }
        printf("%lld\n", ans);
    }
    return 0;
}