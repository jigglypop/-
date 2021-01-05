#include <cstdio>
#include <queue>
#include <cstring>
using namespace std;

int N, M;
int board[100][100] = {
    0,
};
int dy[] = {-1, 1, 0, 0};
int dx[] = {0, 0, 1, -1};

void BFS(int y, int x)
{
    queue<pair<int, int>> q;
    q.push(make_pair(y, x));
    while (!q.empty())
    {
        y = q.front().first;
        x = q.front().second;
        q.pop();
        for (int i = 0; i < 4; i++)
        {
            int ny = y + dy[i];
            int nx = x + dx[i];
            if (0 <= ny < N && 0 <= nx < M)
            {
                if (board[ny][nx] == 1)
                {
                    q.push(make_pair(ny, nx));
                    board[ny][nx] = board[y][x] + 1;
                }
            }
        }
    }
}

int main()
{
    freopen("2178.txt", "r", stdin);
    scanf("%d %d", &N, &M);
    for (int y = 0; y < N; y++)
    {
        for (int x = 0; x < M; x++)
        {
            scanf("%1d", &board[y][x]);
        }
    }
    board[0][0] = 2;
    BFS(0, 0);
    printf("%d\n", board[N - 1][M - 1] - 1);
    return 0;
}