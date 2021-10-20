#include <iostream>
#include <queue>
using namespace std;
int Y, X, K, r, c;
int board[102][102];
pair<int, int> q, di[4] = {{1, 0}, {-1, 0}, {0, -1}, {0, 1}};
queue<pair<int, int>> Q;

int bfs(int sy, int sx) {
    int result = 1;
    board[sy][sx] = 0;
    Q.push(make_pair(sy, sx));
    while (!Q.empty()) {
        int y = Q.front().first;
        int x = Q.front().second;
        Q.pop();
        for (int i = 0; i < 4; i++){
            int ny = y + di[i].first;
            int nx = x + di[i].second;
            if (0 <= ny && ny < Y && 0 <= nx && nx < X) {
                if (board[ny][nx] == 1) {
                    result++;
                    board[ny][nx] = 0;
                    Q.push(make_pair(ny, nx));
                }
            }
        }
    }
    return result;
}

int main() {
    freopen("1743.txt", "r", stdin);
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    cin >> Y >> X >> K;
    for (int k = 0; k < K;k++) {
        cin >> r >> c;
        r--;
        c--;
        board[r][c] = 1;
    }
    int answer = 0;
    for (int y = 0; y < Y;y++) {
        for (int x = 0; x < X;x++) {
            if (board[y][x] == 1) {
                answer = max(answer, bfs(y, x));
            }
        }
    }
    cout << answer;
    return 0;
}
