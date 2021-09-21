#include <iostream>
#include <vector>
#include <queue>
using namespace std;
vector<int> tree[100111];
int parent[100111];
int main()
{
    freopen("parent.txt", "r", stdin);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int n;
    cin >> n;
    for (int i = 0; i < n - 1; i++)
    {
        int u, v;
        cin >> u >> v;
        tree[u].push_back(v);
        tree[v].push_back(u);
    }
    queue<int> Q;
    Q.push(1);
    parent[1] = 0;
    while (!Q.empty())
    {
        int u = Q.front();
        Q.pop();
        for (int v : tree[u])
        {
            if (parent[v] == 0)
            {
                parent[v] = u;
                Q.push(v);
            }
        }
    }
    for (int i = 2; i <= n; i++)
        cout << parent[i] << "\n";
    return 0;
}