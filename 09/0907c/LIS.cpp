#include <iostream>
#include <algorithm>
#include <vector>
#include <memory.h>
using namespace std;

int tc, n;
int cache[501], S[501];

int lis(int start)
{
    int &res = cache[start + 1];
    if (res != -1)
        return res;
    res = 1;
    for (int next = start + 1; next < n; next++)
    {
        if (start == -1 || S[start] < S[next])
        {
            res = max(res, lis(next) + 1);
        }
    }
    return res;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    // freopen("LIS.txt", "r", stdin);
    cin >> tc;
    while (tc--)
    {
        memset(cache, -1, sizeof(cache));
        cin >> n;
        for (int i = 0; i < n; i++)
        {
            cin >> S[i];
        }
        cout << lis(-1) - 1 << '\n';
    }
    return 0;
}