#include <iostream>
#include <queue>
#include <vector>

using namespace std;

struct Edge
{
    int to;
    int cost;
    bool operator<(const Edge &other) const
    {
        return cost > other.cost;
    }
};

vector<Edge> v[1001];
bool check[1001];

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    freopen("1922.txt", "r", stdin);
    int N, M;
    cin >> N >> M;
    for (int i = 0; i < M; i++)
    {
        int from, to, cost;
        cin >> from >> to >> cost;
        v[from].push_back(Edge({to, cost}));
        v[to].push_back(Edge({from, cost}));
    }
    check[1] = true;
    priority_queue<Edge> Q;
    for (Edge e : v[1])
    {
        Q.push(e);
    }
    int ans = 0;
    while (!Q.empty())
    {
        Edge e = Q.top();
        Q.pop();
        if (check[e.to] == true)
        {
            continue;
        }
        check[e.to] = true;
        ans += e.cost;
        int x = e.to;
        for (Edge ee : v[x])
        {
            Q.push(ee);
        }
    }
    cout << ans << "\n";
    return 0;
}