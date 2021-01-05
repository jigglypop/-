#include <cstring>
#include <iostream>
#include <string>
using namespace std;
int alpha[26];
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    freopen("10808.txt", "r", stdin);
    string S;
    cin >> S;
    for (int i = 0; i < S.size(); i++)
    {
        alpha[S[i] - 'a']++;
    }
    for (auto a : alpha)
    {
        cout << a << " ";
    }
    return 0;
}