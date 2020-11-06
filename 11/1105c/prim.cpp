#include <cstring>
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

struct Edge
{
    int u, cost;
    bool operator<(const Edge &other) const
    {
        return cost > other.cost;
    }
};

vector<Edge> graph[1001];
bool check[1001];
int main()
{
    freopen("prim.txt", "r", stdin);
    int N, M;
    scanf("%d", &N);
    scanf("%d", &M);
    for (int i = 0; i < M; i++)
    {
        int a, b, cost;
        scanf("%d %d %d", &a, &b, &cost);
        graph[a].push_back(Edge({b, cost}));
        graph[b].push_back(Edge({a, cost}));
    }
    check[1] = true;
    priority_queue<Edge> PQ;
    for (Edge e : graph[1])
    {
        PQ.push(e);
    }
    int result = 0;
    while (!PQ.empty())
    {
        Edge pq = PQ.top();
        PQ.pop();
        int u = pq.u;
        int cost = pq.cost;
        if (check[u])
        {
            continue;
        }
        check[u] = true;
        result += cost;
        for (Edge v : graph[u])
        {
            PQ.push(v);
        }
    }
    printf("%d\n", result);
    return 0;
}