#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;

int N;
int board[4][4];
bool check[4][4];
pair<int, int> q, di[4] = {{1, 0}, {0, 1}};
queue<pair<int, int>> Q;

string bfs() {
    Q.push(make_pair(0, 0));
    check[0][0] = true;
    while (!Q.empty()) {
        q = Q.front();
        Q.pop();
        int y = q.first;
        int x = q.second;
        if (board[y][x] == -1) {
            return "HaruHaru";
        }
        int n = board[y][x];
        for (int i = 0; i < 4;i++){
            int ny = y + di[i].first * n;
            int nx = x + di[i].second * n;
            if (0 <= ny && ny < N && 0 <= nx && nx < N) {
                if (!check[ny][nx]) {
                    check[ny][nx] = true;
                    Q.push(make_pair(ny, nx));
                }
            }
        }
    }
    return "Hing";
}

int main() {
    freopen("16173.txt", "r", stdin);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> N;
    for (int y = 0; y < N; y++){
        for (int x = 0; x < N; x++){
            cin >> board[y][x];
        }
    }
    cout << bfs();
    return 0;
}