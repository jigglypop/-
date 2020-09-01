#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#include <cstring>

using namespace std;

vector<int> dfs_order;
vector<int> first;
vector<int> level;
vector<int> a[10001];

void dfs(int node, int parent, int depth)
{
    dfs_order.push_back(node);
    level.push_back(depth);
    for (int child : a[node])
    {
        if (child == parent)
            continue;
        dfs(child, node, depth + 1);
        dfs_order.push_back(node);
        level.push_back(depth);
    }
}

int main()
{
    freopen("11438.txt", "r", stdin);
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int u, v;
        cin >> u >> v;
        a[u].push_back(v);
        a[v].push_back(u);
    }

    return 0;
}