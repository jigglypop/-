#include <iostream>
#include <queue>
using namespace std;
queue<pair<int, int>>q;
int st, ed, jump[10001], roof, vis[10001], swc, res;
int main() {
    freopen("1326.txt", "r", stdin);
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
	cin >> roof;
	for (int i = 1; i <= roof; i++) {
		cin >> jump[i]; 
	}
	cin >> st;
	cin >> ed;
	q.push(make_pair(st, 0));
	vis[st] = 1;
	while (!q.empty()) {
		if (q.front().first == ed) {
			res = q.front().second;
			swc++; 
			break;
		}
		int now = q.front().first; 
		int cnt = q.front().second; 
		q.pop();
		for (int i = 1; now + (jump[now] * i) <= roof; i++) {
			int next = now + jump[now] * i;
			if (vis[next] == 0) {
				vis[next] = 1;
				q.push(make_pair(next, cnt + 1));
			}
		}
		for (int i = 1; now - (jump[now] * i) >= 1; i++) {
			int next = now - jump[now] * i;
			if (vis[next] == 0) {
				vis[next] = 1;
				q.push(make_pair(next, cnt + 1));
			}
		}
	}
	if (swc == 0) {
		cout << -1;
	}
	else cout << res; 
}