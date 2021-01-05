#include <iostream>
#include <cstring>

int Y, X;
int DP[501][501];
int A[501][501];
int dy[4] = {-1, 1, 0, 0};
int dx[4] = {0, 0, -1, 1};

int dfs(int y, int x)
{
    if (DP[y][x] != -1)
    {
        return DP[y][x];
    }
    if (x == X - 1 && y == Y - 1)
    {
        return 1;
    }
    int &result = DP[y][x];
    result = 0;
    for (int i = 0; i < 4; i++)
    {
        int ny = y + dy[i];
        int nx = x + dx[i];
        if (0 <= ny && ny < Y && 0 <= nx && nx < X)
        {
            if (A[y][x] > A[ny][nx])
            {
                result += dfs(ny, nx);
            }
        }
    }
    return result;
}

int main()
{
    freopen("1520.txt", "r", stdin);
    scanf("%d %d", &Y, &X);
    for (int y = 0; y < Y; y++)
    {
        for (int x = 0; x < X; x++)
        {
            scanf("%d ", &A[y][x]);
        }
    }
    memset(DP, -1, sizeof(DP));
    dfs(0, 0);
    printf("%d", DP[0][0]);
    // for (int y = 0; y < Y; y++)
    // {
    //     for (int x = 0; x < X; x++)
    //     {
    //         printf("%d ", DP[y][x]);
    //     }
    //     printf("\n");
    // }
    return 0;
}