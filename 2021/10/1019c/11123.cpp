#include <iostream>
#include <algorithm>
#include <queue>
#include <string.h>
using namespace std;

int  sum;
char board[102][102];
bool check[102][102];
queue <pair<int, int>> Q;
pair<int, int> q, p[4] = {{1,0}, {-1,0}, {0,1}, {0,-1} };
void bfs() {
	while (Q.empty() != true) {
		q = Q.front();
		Q.pop();
        int y = q.first;
        int x = q.second;
        for (int i = 0;i < 4;i++) {
            int ny = y + p[i].first;
            int nx = x + p[i].second;
            if (board[ny][nx] == '#' && check[ny][nx] == true) {
				Q.push(make_pair(ny, nx));
				check[ny][nx] = false;
			}
		}
	}
	sum++;
	return;
}
int main() {
    freopen("11123.txt", "r", stdin);
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int t;
	int x = 1, y = 1;
	cin >> t;
	while(t--) {
		cin >> y >> x;
		sum = 0;
		for (int i = 0; i < 102;i++) {
			memset(board[i], 0, sizeof(char) * 102);
			memset(check[i], true, sizeof(bool) * 102);
		}
		for (int j = 1;j <= y;j++)
			for (int i = 1;i <= x;i++) {
				cin >> board[j][i];
			}

		for (int j = 1;j <= y;j++)
			for (int i = 1;i <= x;i++) {
				if (board[j][i] == '#' && check[j][i] == true) {
					Q.push(make_pair(j, i));
					check[j][i] = false;
					bfs();
				}
			}
		cout << sum << '\n';
	}
	return 0;
}