#include <iostream>
#include <algorithm>
using namespace std;
int W[11];
int K[11];

int main() {
    freopen("5576.txt", "r", stdin);
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    for (int i = 0; i < 10;i++){
        cin >> W[i];
    }
    for (int i = 0; i < 10;i++){
        cin >> K[i];
    }
    sort(W, W + 10);
    sort(K, K + 10);
    cout << W[9] + W[8] + W[7] << " " << K[9] + K[8] + K[7];
    return 0;
}
