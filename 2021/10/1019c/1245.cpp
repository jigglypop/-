#include <iostream>
#include <algorithm>
#include <queue>

using namespace std;
int Y, X, flag;
int board[102][102];
bool check[102][102];
queue <pair<int, int>> Q;
pair<int, int> q, di[4] = {{1,0}, {-1,0}, {0,1}, {0,-1}};

void bfs(int sy, int sx) {
    cout << flag;
    while (!Q.empty()){

    }
}

int main() {
    freopen("1245.txt", "r", stdin);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> Y >> X;
    for (int y = 0; y < Y; y++){
        for (int x = 0; x < X; x++){
            cin >> board[y][x];
        }
    }
    for (int y = 0; y < Y; y++){
        for (int x = 0; x < X; x++){
            if (check[y][x] == false && board[y][x] != 0) {
                flag++;
                check[y][x] = true;
                bfs(y, x);
            }
        }
    }

    for (int y = 0; y < Y; y++){
        for (int x = 0; x < X; x++){
            cout << check[y][x];
        }
        cout << endl;
    }
    return 0;
}

