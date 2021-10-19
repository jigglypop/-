#include <iostream>
using namespace std;
long long N;
long long nums[100002];

int main() {
    freopen("11868.txt", "r", stdin);
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    cin >> N;
    int S = 0;
    for (int i = 0; i < N;i++) {
        int p;
        cin >> p;
        S ^= p;
    }
    if (S != 0) {
        cout << "koosaga";
    } else {
        cout << "cubelover";        
    }
    return 0;
}