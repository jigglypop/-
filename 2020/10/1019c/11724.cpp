#include <cstdio>
#include <vector>

using namespace std;
vector<int> graph[1001];
bool visited[1001];
void dfs(int u)
{
    visited[u] = true;
    for (int i = 0; i < graph[u].size(); i++)
    {
        int v = graph[u][i];
        if (visited[v] == false)
        {
            dfs(v);
        }
    }
}
int main()
{
    freopen("11724.txt", "r", stdin);
    int n, m;
    scanf("%d %d", &n, &m);
    for (int i = 0; i < m; i++)
    {
        int u, v;
        scanf("%d %d", &u, &v);
        graph[u].push_back(v);
        graph[v].push_back(u);
    }
    int result = 0;
    for (int i = 1; i <= n; i++)
    {
        if (visited[i] == false)
        {
            dfs(i);
            result++;
        }
    }
    printf("%d\n", result);
    return 0;
}
