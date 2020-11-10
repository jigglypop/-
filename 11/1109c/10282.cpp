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

int INF = 1e9;

int main()
{
    freopen("10282.txt", "r", stdin);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int T;
    cin >> T;
    while (T--)
    {
        vector<Edge> A[10001];
        int dist[10001];
        bool check[10001];
        int n, d, start;
        cin >> n >> d >> start;
        for (int i = 0; i < d; i++)
        {
            int a, b, c;
            cin >> a >> b >> c;
            A[b].push_back(Edge(a, c));
        }
        for (int i = 1; i <= n; i++)
            dist[i] = INF;
        dist[start] = 0;
        priority_queue<pair<int, int>> PQ;
        PQ.push(make_pair(0, start));
        while (!PQ.empty())
        {
            auto pq = PQ.top();
            PQ.pop();
            int u = pq.second;
            if (dist[u] < pq.first)
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
        int cnt = 0, time = 0;
        for (int i = 1; i <= n; i++)
        {
            if (dist[i] != INF)
            {
                cnt++;
                if (time < dist[i])
                    time = dist[i];
            }
        }
        cout << cnt << " " << time << "\n";
    }
    return 0;
}