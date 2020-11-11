#include <iostream>
#include <cstdio>
#include <vector>
#include <cstring>
using namespace std;
vector<pair<int, int>> graph[10001];
bool check[10001];
int n, m;
int S, E;
bool dfs(int node, int limit)
{
    if (check[node])
        return false;
    check[node] = true;
    if (node == E)
        return true;
    for (auto &p : graph[node])
    {
        int next = p.first;
        int cost = p.second;
        if (cost >= limit)
        {
            if (dfs(next, limit))
                return true;
        }
    }
    return false;
}
int main()
{
    freopen("1939.txt", "r", stdin);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n >> m;
    while (m--)
    {
        int x, y, z;
        cin >> x >> y >> z;
        graph[x].push_back(make_pair(y, z));
        graph[y].push_back(make_pair(x, z));
    }
    cin >> S >> E;
    int left, right;
    left = 1;
    right = 1000000000;
    int ans = 0;
    while (left <= right)
    {
        int mid = left + (right - left) / 2;
        memset(check, false, sizeof(check));
        if (dfs(S, mid))
        {
            ans = mid;
            left = mid + 1;
        }
        else
            right = mid - 1;
    }
    cout << ans << "\n";
    return 0;
}