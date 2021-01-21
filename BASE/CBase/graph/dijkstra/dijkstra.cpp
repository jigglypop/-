#include <iostream>
#include <vector>
#include <queue>
using namespace std;
struct Edge
{
    int to;
    int cost;
    Edge(int to, int cost) : to(to), cost(cost)
    {
    }
};
vector<Edge> A[20001];
int dist[20001];
bool check[20001];
int INF = 1e9;

int main()
{
    freopen("dijkstra.txt", "r", stdin);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int N, M;
    cin >> N >> M;
    int start;
    cin >> start;
    for (int i = 0; i < M; i++)
    {
        int a, b, c;
        cin >> a >> b >> c;
        A[a].push_back(Edge(b, c));
    }
    for (int i = 1; i <= N; i++)
        dist[i] = INF;
    dist[start] = 0;
    priority_queue<pair<int, int>> PQ;
    PQ.push(make_pair(0, start));
    while (!PQ.empty())
    {
        auto pq = PQ.top();
        PQ.pop();
        int u = pq.second;
        if (check[u])
            continue;
        check[u] = true;
        for (int i = 0; i < A[u].size(); i++)
        {
            int v = A[u][i].to;
            if (dist[v] > dist[u] + A[u][i].cost)
            {
                dist[v] = dist[u] + A[u][i].cost;
                PQ.push(make_pair(-dist[v], v));
            }
        }
    }
    for (int i = 1; i <= N; i++)
    {
        if (dist[i] >= INF)
            printf("INF\n");
        else
            printf("%d\n", dist[i]);
    }
    return 0;
}