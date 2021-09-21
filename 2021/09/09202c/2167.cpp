#include <cstdio>
#include <queue>
#include <cstring>
using namespace std;
int board[301][301];
int dp[302][302];
int main()
{
    freopen("2167.txt", "r", stdin);
    int Y, X;
    scanf("%d %d", &Y, &X);
    for (int y = 0; y < Y;y++) {
        for (int x = 0; x < X;x++) {
            scanf("%d", &board[y][x]);
        }
        scanf("\n");
    }
    for (int y = 1; y <= Y;y++) {
        for (int x = 1; x <= X;x++) {
            dp[y][x] += board[y - 1][x - 1] + dp[y - 1][x] + dp[y][x - 1] - dp[y - 1][x - 1];
        }
        scanf("\n");
    }
    int M;
    scanf("%d", &M);
    while(M--) {
        int sy, sx, ey, ex;
        scanf("%d %d %d %d", &sy, &sx, &ey, &ex);
        printf("%d\n", dp[ey][ex] - dp[sy - 1][ex] - dp[ey][sx - 1] + dp[sy - 1][sx - 1]);
    }
    return 0;
}