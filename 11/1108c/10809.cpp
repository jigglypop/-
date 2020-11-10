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
    freopen("10809.txt", "r", stdin);
    memset(alpha, -1, sizeof(alpha));
    string S;
    cin >> S;
    for (int i = 0; i < S.size(); i++)
    {
        if (alpha[S[i] - 'a'] == -1)
            alpha[S[i] - 'a'] = i;
    }
    for (auto a : alpha)
    {
        cout << a << " ";
    }
    return 0;
}