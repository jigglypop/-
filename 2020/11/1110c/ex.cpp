// #include <cstring>
#include <iostream>
// #include <string>
#include <stack>
using namespace std;
long long A[100000];
int main()
{
    freopen("6549.txt", "r", stdin);
    cin.sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    while (true)
    {
        int N;
        cin >> N;
        if (N == 0)
            break;
        for (int i = 0; i < N; i++)
            cin >> A[i];
        stack<long long> S;
        long long ans = 0;
        A[N] = -1;
        for (int i = 0; i < N + 1; i++)
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
        cout << ans << "\n";
    }
    return 0;
}