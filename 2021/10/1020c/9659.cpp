#include <iostream>
using namespace std;
long long N;
int main() {
    freopen("9659.txt", "r", stdin);
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    cin >> N;
    if (N % 2) cout << "SK\n";
    else
        cout << "CY\n";
    return 0;
}
