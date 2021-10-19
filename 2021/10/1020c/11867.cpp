#include <iostream>
using namespace std;
long long N, M;
int main() {
    freopen("11867.txt", "r", stdin);
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    cin >> N >> M;
    if (N % 2 || M % 2) cout << "A\n";
    else
        cout << "B\n";
    return 0;
}
