#include <iostream>
#include <cstring>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int main()
{
    freopen("2109.txt", "r", stdin);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int n;
    vector<pair<int, int>> A;
    priority_queue<int> PQ;
    cin >> n;
    for (int i = 0; i < n; ++i)
    {
        int a, b;
        cin >> a >> b;
        A.push_back(make_pair(b, a));
    }
    sort(A.begin(), A.end());
    int ans = 0;
    for (int i = 0; i < n; i++)
    {
        ans += A[i].second;
        PQ.push(-A[i].second);
        if (PQ.size() > A[i].first)
        {
            ans += PQ.top();
            PQ.pop();
        }
    }
    cout << ans;
    return 0;
}
