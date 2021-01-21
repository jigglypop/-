#include <cstring>
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;
struct Edge
{
    int from, to, cost;
    bool operator<(const Edge &other) const
    {
        return cost < other.cost;
    }
};
int parent[10001];
int Find(int x)
{
    if (x == parent[x])
    {
        return x;
    }
    else
    {
        return parent[x] = Find(parent[x]);
    }
}
void Union(int x, int y)
{
    x = Find(x);
    y = Find(y);
    if (y >= x)
    {
        parent[x] = y;
    }
    else
    {
        parent[y] = x;
    }
}
int main()
{
    freopen("kruskal.txt", "r", stdin);
    int n, m;
    scanf("%d", &n);
    scanf("%d", &m);

    for (int i = 1; i <= n; i++)
    {
        parent[i] = i;
    }
    vector<Edge> graph(m);
    for (int i = 0; i < m; i++)
    {
        scanf("%d %d %d", &graph[i].from, &graph[i].to, &graph[i].cost);
    }
    sort(graph.begin(), graph.end());
    int ans = 0;
    for (int i = 0; i < m; i++)
    {
        Edge e = graph[i];
        int x = Find(e.from);
        int y = Find(e.to);
        if (x != y)
        {
            Union(e.from, e.to);
            ans += e.cost;
        }
    }
    printf("%d\n", ans);
    return 0;
}