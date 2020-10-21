#include <cstdio>
#include <algorithm>
#include <queue>

using namespace std;
int board[30][30];
int visited[30][30];
int dy[] = {0, 0, 1, -1};
int dx[] = {1, -1, 0, 0};
int N;
int ans[25 * 25];

void bfs(int y, int x, int cnt)
{
    queue<pair<int, int>> Q;
    Q.push(make_pair(y, x));
    visited[y][x] = cnt;
    while (!Q.empty())
    {
        y = Q.front().first;
        x = Q.front().second;
        Q.pop();
        for (int i = 0; i < 4; i++)
        {
            int ny = y + dy[i];
            int nx = x + dx[i];
            if (0 <= nx && nx < N && 0 <= ny && ny < N)
            {
                if (board[ny][nx] == 1 && visited[ny][nx] == 0)
                {
                    Q.push(make_pair(ny, nx));
                    visited[ny][nx] = cnt;
                }
            }
        }
    }
}

int main()
{
    freopen("./2667.txt", "r", stdin);
    scanf("%d", &N);
    for (int y = 0; y < N; y++)
    {
        for (int x = 0; x < N; x++)
        {
            scanf("%1d", &board[y][x]);
        }
    }
    int cnt = 0;

    for (int y = 0; y < N; y++)
    {
        for (int x = 0; x < N; x++)
        {
            if (board[y][x] == 1 && visited[y][x] == 0)
            {
                bfs(y, x, ++cnt);
            }
        }
    }
    printf("%d\n", cnt);
    for (int y = 0; y < N; y++)
    {
        for (int x = 0; x < N; x++)
        {
            ans[visited[y][x]] += 1;
        }
    }
    sort(ans + 1, ans + cnt + 1);
    for (int i = 1; i <= cnt; i++)
    {
        printf("%d\n", ans[i]);
    }
    return 0;
}