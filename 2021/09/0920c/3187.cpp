#include <stdio.h>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;
char board[251][251];
int Y, X;
int dy[4] = {0, 0, 1, -1};
int dx[4] = {1, -1, 0, 0};
int K_size = 0;
int V_size = 0;

void bfs(int sy, int sx)
{
    queue<pair<int, int>> Q;
    Q.push(make_pair(sy, sx));
    int K = 0;
    int V = 0;
    if (board[sy][sx] == 'k') {
        K++;
    } else if (board[sy][sx] == 'v') {
        V++;
    }
    board[sy][sx] = '#';
    while (!Q.empty()){
        pair<int, int> q = Q.front();
        Q.pop();
        for (int i = 0; i < 4;i++) {
            int ny = q.first + dy[i];
            int nx = q.second + dx[i];
            if (0 <= ny && ny < Y && 0 <= nx && nx < X) {
                if (board[ny][nx] != '#') {
                    if (board[ny][nx] == 'k') {
                        K++;
                    } else if (board[ny][nx] == 'v') {
                        V++;
                    }
                    board[ny][nx] = '#';
                    Q.push(make_pair(ny, nx));
                }
            }
        }
    }
    if (K > V) {
        K_size += K;
    } else {
        V_size += V;
    }
}

int main()
{
    freopen("3187.txt", "r", stdin);
    scanf("%d %d\n", &Y, &X);
    for (int y = 0; y < Y;y++){
        for (int x = 0; x < X;x++){
            scanf("%c", &board[y][x]);
        }   
        scanf("\n");   
    }

    for (int y = 0; y < Y;y++){
        for (int x = 0; x < X;x++){
            if (board[y][x] != '#') {
                bfs(y, x);
            }
        }   
    }
    printf("%d %d", K_size, V_size);
    return 0;
}