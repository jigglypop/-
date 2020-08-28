#include <cstdio>
#include <algorithm>
#include <queue>
#include <vector>

using namespace std;

struct Edge
{
    int from, to, cost;
    bool operator<(const Edge &other) const
    {
        return cost < other.cost;
    }
};
int p[10001];

int Find(int x)
{
    if (x == p[x])
    {
        return x;
    }
    else
    {
        return p[x] = Find(p[x]);
    }
}

void Union(int x, int y)
{
    x = Find(x);
    y = Find(y);
    p[x] = y;
}

int main()
{
    freopen("1197.txt", "r", stdin);
    int N, M;
    scanf("%d %d", &N, &M);
    for (int n = 0; n < N; n++)
    {
        p[n] = n;
    }
    vector<Edge> v(M);
    for (int m = 0; m < M; m++)
    {
        scanf("%d %d %d", &v[m].from, &v[m].to, &v[m].cost);
    }
    sort(v.begin(), v.end());
    int ans = 0;
    for (int i = 0; i < M; i++)
    {
        Edge e = v[i];
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