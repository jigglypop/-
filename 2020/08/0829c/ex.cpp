#include <cstdio>
#include <vector>
#include <queue>
using namespace std;

struct Edge
{
    int to;
    int cost;
    Edge(int to, int cost) : to(to), cost(cost) {}
};

vector<Edge> graph[20001];
int dist[20001];
bool check[20001];
int inf = 1000000000;

int main()
{
    freopen("1753.txt", "r", stdin);
    int V, E;
    scanf("%d %d", &V, &E);
    int start;
    scanf("%d", &start);
    for (int i = 0; i < E; i++)
    {
        int a, b, c;
        scanf("%d %d %d", &a, &b, &c);
        graph[a].push_back(Edge(b, c));
    }
    for (int i = 1; i <= V; i++)
    {
        dist[i] = inf;
    }
    dist[start] = 0;
    priority_queue<pair<int, int>> Q;
    Q.push(make_pair(0, start));
    while (!Q.empty())
    {
        auto p = Q.top();
        Q.pop();
        int u = p.second;
        if (check[u])
        {
            continue;
        }
        check[u] = true;
        for (int i = 0; i < graph[u].size(); i++)
        {
            int v = graph[u][i].to;
            if (dist[v] > dist[u] + graph[u][i].cost)
            {
                dist[v] = dist[u] + graph[u][i].cost;
                Q.push(make_pair(-dist[v], v));
            }
        }
    }
    for (int i = 1; i <= V; i++)
    {
        if (dist[i] >= inf)
        {
            printf("INF\n");
        }
        else
        {
            printf("%d\n", dist[i]);
        }
    }
    return 0;
}