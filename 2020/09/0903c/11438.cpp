#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

const int MAX = 100111;
vector<int> a[MAX];
int p[MAX][17];
int tin[MAX];
int tout[MAX];
int timer;
int l;
void dfs(int v, int parent)
{
    tin[v] = ++timer;
    p[v][0] = parent;
    for (int i = 1; i <= l; i++)
    {
        p[v][i] = p[p[v][i - 1]][i - 1];
    }
    for (int to : a[v])
    {
        if (to != parent)
        {
            dfs(to, v);
        }
    }
    tout[v] = ++timer;
}
bool upper(int u, int v)
{
    return (tin[u] <= tin[v] && tout[u] >= tout[v]);
}
int lca(int u, int v)
{
    if (upper(u, v))
        return u;
    if (upper(v, u))
        return v;
    for (int i = l; i >= 0; i--)
    {
        if (!upper(p[u][i], v))
        {
            u = p[u][i];
        }
    }
    return p[u][0];
}
int main()
{
    freopen("11438.txt", "r", stdin);
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
    for (l = 1; (1 << l) <= n; l++)
    {
    }
    dfs(1, 1);
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