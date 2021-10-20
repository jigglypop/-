#include <iostream>
#include <algorithm>
#include <string>
#include <set>
using namespace std;
int N;
set<int> S;

int main() {
    freopen("10867.txt", "r", stdin);
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    cin >> N;
    for (int i = 0; i < N;i++){
        int s;
        cin >> s;
        S.insert(s);
    }
    set<int>::iterator iter;
    for (iter = S.begin();iter != S.end();iter++) {
        cout << *iter << " ";
    }
    return 0;
}