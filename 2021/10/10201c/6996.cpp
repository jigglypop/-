#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
string a, b, c, d;
int N;

int main() {
    freopen("6996.txt", "r", stdin);
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    cin >> N;
    while (N--) {
        cin >> c >> d;
        a = c;
        b = d;
        sort(a.begin(), a.end());
        sort(b.begin(), b.end());
        cout << c << " & " << d << " are ";
        if (a != b) {
            cout << "NOT ";
        }
        cout << "anagrams." << endl;
    }
    return 0;
}