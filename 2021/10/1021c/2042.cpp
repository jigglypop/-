#include <iostream>
#include <algorithm>
#include <string>
#define MAX 1000001
using namespace std;
typedef long long ll;
int n;  
ll t[2 * MAX];

void init() {  
	for (int i = n - 1; i > 0; i--) {
        t[i] = t[i << 1] + t[i << 1 | 1];
    } 
}

void update(int p, ll val) {  
	for (t[p += n] = val; p > 1; p >>= 1) t[p >> 1] = t[p] + t[p ^ 1];
}

ll query(int l, int r) {  
	ll res = 0;
	for (l += n, r += n; l < r; l >>= 1, r >>= 1) {
		if (l & 1) res += t[l++];
		if (r & 1) res += t[--r];
	}
	return res;
}

int main() {
    freopen("2042.txt", "r", stdin);
	ios::sync_with_stdio(false);
	cin.tie(0);	
	int M, K;
	cin >> n >> M >> K;
	for (int i = 0; i < n; ++i) cin >> t[n + i];
	init();
	for(int i = 0; i < M + K; i++) {
		ll x, y, z;
		cin >> x >> y >> z;
		if(x == 1) update(y - 1, z);
		else cout << query(y - 1, z) << '\n';
	}
	return 0;
}