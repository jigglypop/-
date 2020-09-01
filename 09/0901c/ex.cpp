#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <cstring>

using namespace std;
const int MAX = 100111;
vector<int> tree[MAX];
int parent[MAX];
bool check[MAX];
int depth[MAX];

int LCA(int u, int v)
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
        tree[u].push_back(v);
        tree[v].push_back(u);
    }
    depth[1] = 0;
    check[1] = true;
    queue<int> Q;
    Q.push(1);
    parent[1] = 0;
    while (!Q.empty())
    {
        int x = Q.front();
        Q.pop();
        for (int y : tree[x])
        {
            if (!check[y])
            {
                depth[y] = depth[x] + 1;
                check[y] = true;
                parent[y] = x;
                Q.push(y);
            }
        }
    }
    int m;
    cin >> m;
    while (m--)
    {
        int u, v;
        cin >> u >> v;
        cout << LCA(u, v) << "\n";
    }

    return 0;
}