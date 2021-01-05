#include <iostream>
#include <cstring>
#include <vector>
#include <queue>
using namespace std;
vector<int> graph[32001];
int indegree[32001];
int main()
{
    freopen("DAG.txt", "r", stdin);
    int N, M;
    scanf("%d %d", &N, &M);
    for (int i = 0; i < M; i++)
    {
        int a, b;
        scanf("%d %d", &a, &b);
        graph[a].push_back(b);
        indegree[b]++;
    }
    queue<int> Q;
    for (int i = 1; i <= N; i++)
    {
        if (indegree[i] == 0)
        {
            Q.push(i);
        }
    }
    while (!Q.empty())
    {
        int u = Q.front();
        Q.pop();
        for (int v : graph[u])
        {
            indegree[v]--;
            if (indegree[v] == 0)
            {
                Q.push(v);
            }
        }
        printf("%d ", u);
    }
    return 0;
}