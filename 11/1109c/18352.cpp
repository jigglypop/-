#include <iostream>
#include <queue>
#include <vector>
using namespace std;

struct Edge
{
    int to;
    int cost;
    Edge(int to, int cost) : to(to), cost(cost)
    {
    }
};
vector<Edge> graph[300001];
int dist[300001];
int INF = 1e9;

int main()
{
    freopen("18352.txt", "r", stdin);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int N, M, K, X;
    cin >> N >> M >> K >> X;
    for (int i = 0; i < M; i++)
    {
        int a, b;
        cin >> a >> b;
        graph[a].push_back(Edge(b, 1));
        graph[b].push_back(Edge(a, 1));
    }
    for (int i = 0; i <= N; i++)
    {
        dist[i] = INF;
    }
    dist[X] = 0;
    priority_queue<pair<int, int>> PQ;
    PQ.push(make_pair(0, X));
    while (!PQ.empty())
    {
        auto pq = PQ.top();
        PQ.pop();
        int u = pq.second;
        if (dist[u] < pq.first)
            continue;
        for (int i = 0; i < graph[u].size(); i++)
        {
            int v = graph[u][i].to;
            if (dist[v] > dist[u] + graph[u][i].cost)
            {
                dist[v] = dist[u] + graph[u][i].cost;
                PQ.push(make_pair(-dist[v], v));
            }
        }
    }
    int count = 0;
    for (int i = 1; i <= N; i++)
    {
        if (dist[i] == K)
        {
            cout << i << "\n";
            count += 1;
        }
    }
    if (count == 0)
        cout << -1 << "\n";
    return 0;
}