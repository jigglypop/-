#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;
int n, m, board[301][301], dp[301][301];
int main() {
    freopen("17391.txt", "r", stdin);
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
	cin >> n >> m;
	for (int i = 0; i < n; ++i) for (int j = 0; j < m; ++j) cin >> board[i][j];
	memset(dp, 0, sizeof(dp));
	dp[0][0] = 1;
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			for (int k = 1; k <= board[i][j]; ++k) {
				if (i + k < n) {
					if (!dp[i + k][j]) dp[i + k][j] = dp[i][j] + 1;
					else dp[i + k][j] = min(dp[i + k][j], dp[i][j] + 1);
				}
				if (j + k < m) {
					if (!dp[i][j + k]) dp[i][j + k] = dp[i][j] + 1;
					else dp[i][j + k] = min(dp[i][j + k], dp[i][j] + 1);
				}
			}
		}
	}
	cout << dp[n - 1][m - 1] - 1;
}