#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;
const int MAX = 100111;
vector<int> a[MAX];
int parent[MAX];
bool check[MAX];
int depth[MAX];
int lca(int u, int v)
{
    if (depth[u] < depth[v])
    {
        swap(u, v);
    }
    while (depth[u] != depth[v])
    {
        u = parent[u];
    }
    while (u != v)
    {
        u = parent[u];
        v = parent[v];
    }
    return u;
}
int main()
{
    freopen("11437.txt", "r", stdin);
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    for (int i = 0; i < n - 1; i++)
    {
        int u, v;
        cin >> u >> v;
        a[u].push_back(v);
        a[v].push_back(u);
    }
    depth[1] = 0;
    check[1] = true;
    queue<int> q;
    q.push(1);
    parent[1] = 0;
    while (!q.empty())
    {
        int x = q.front();
        q.pop();
        for (int y : a[x])
        {
            if (!check[y])
            {
                depth[y] = depth[x] + 1;
                check[y] = true;
                parent[y] = x;
                q.push(y);
            }
        }
    }
    int m;
    cin >> m;
    while (m--)
    {
        int u, v;
        cin >> u >> v;
        cout << lca(u, v) << '\n';
    }
    return 0;
}