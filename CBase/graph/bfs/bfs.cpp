#include <cstring>
#include <algorithm>
#include <vector>
#include <iostream>
#include <queue>
using namespace std;
vector<int> graph[1001];
bool visited[1001];

void bfs(int start)
{
    queue<int> Q;
    memset(visited, false, sizeof(visited));
    visited[start] = true;
    Q.push(start);
    while (!Q.empty())
    {
        int u = Q.front();
        Q.pop();
        printf("%d ", u);
        for (int i = 0; i < graph[u].size(); i++)
        {
            int v = graph[u][i];
            if (visited[v] == false)
            {
                visited[v] = true;
                Q.push(v);
            }
        }
    }
}

int main()
{
    freopen("./bfs.txt", "r", stdin);
    int N, M, start;
    scanf("%d %d %d", &N, &M, &start);
    for (int i = 0; i < M; i++)
    {
        int u, v;
        scanf("%d %d", &u, &v);
        graph[u].push_back(v);
        graph[v].push_back(u);
    }
    for (int i = 1; i <= N; i++)
    {
        sort(graph[i].begin(), graph[i].end());
    }
    bfs(start);
    return 0;
}