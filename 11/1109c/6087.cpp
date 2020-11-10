#include <iostream>
#include <queue>
#include <cstring>
using namespace std;
char graph[101][101];
int dy[] = {-1, 1, 0, 0};
int dx[] = {0, 0, -1, 1};
int visited[101][101][4];
int main()
{
    freopen("6087.txt", "r", stdin);
    int X, Y;
    cin >> X >> Y;
    int sy, sx;
    for (int y = 0; y <= Y; y++)
    {
        for (int x = 0; x < X; x++)
        {
            char temp;
            cin >> temp;
            graph[y][x] = temp;
            if (temp == 'C')
            {
                sy = y;
                sx = x;
            }
        }
    }
    for (int i = 0; i < 4; i++)
        visited[sy][sx][i] = 1;
    queue<pair<int, int>> Q;
    Q.push(make_pair(sy, sx));
    while (!Q.empty())
    {
        int y = Q.front().first;
        int x = Q.front().second;
        Q.pop();
        for (int i = 0; i < 4; i++)
        {
            int ny = y + dy[i];
            int nx = x + dx[i];
            if (0 <= ny && ny < Y && 0 <= nx && nx < X)
            {
                if (visited[ny][nx] == 0){
                    
                }
            }
        }
    }

    // for (int y = 0; y <= Y; y++)
    // {
    //     for (int x = 0; x < X; x++)
    //     {
    //         cout << graph[y][x] << " ";
    //     }
    //     cout << "\n";
    // }
}