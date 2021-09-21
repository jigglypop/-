#include <stdio.h>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;
typedef long long ll;
int N;
ll board[1001][1001];
int parent[1001];

struct Edge {
    ll w;
    int a, b;
};

int find(int x) {
    if (parent[x] != x) {
        parent[x] = find(parent[x]);
    }
    return parent[x];
}

bool merge(int x, int y){
    x = find(x);
    y = find(y);
    if (x == y)
        return false;
    parent[x] = y;
    return true;
}

int main()
{
    freopen("16398.txt", "r", stdin);
    scanf("%d", &N);
    vector<Edge> edge;
    for (int i = 0; i < N;i++) {
        for (int j = 0; j < N;j++) {
            ll value;
            scanf("%lld ", &value);
            if (j > i) {
                Edge eg;
                eg.a = i;
                eg.b = j;
                eg.w = value;
                edge.push_back(eg);
            }
            board[i][j] = value;
        }   
        scanf("\n");    
    }
    for (int i = 0; i < N;i++) {
        parent[i] = i;
    }
    sort(edge.begin(), edge.end(), [&](Edge a, Edge b) {
		return a.w < b.w;
	});
    ll ans = 0;
    for (auto &eg: edge) {
        int A = eg.a;
        int B = eg.b;
        int W = eg.w;
        int a = find(eg.a);
        int b = find(eg.b);
        if (a != b) {
            merge(a, b);
            ans += W;
        }
    }
    printf("%lld", ans);
    return 0;
}