#include <iostream>
#include <cstring>
#include <vector>

using namespace std;
using namespace std;

int main()
{
    freopen("luca.txt", "r", stdin);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    long long n, r, p;
    cin >> n >> r >> p;
    vector<vector<int>> d(p + 1, vector<int>(p + 1));
    for (int i = 0; i <= p; i++)
    {
        d[i][0] = d[i][i] = 1;
        for (int j = 1; j <= i - 1; j++)
        {
            d[i][j] = d[i - 1][j - 1] + d[i - 1][j];
            d[i][j] %= p;
        }
    }
    vector<int> a, b;
    while (n > 0 || r > 0)
    {
        a.push_back(n % p);
        b.push_back(r % p);
        n /= p;
        r /= p;
    }
    long long ans = 1;
    for (int i = 0; i < a.size(); i++)
    {
        ans *= d[a[i]][b[i]];
        ans %= p;
    }
    cout << ans << '\n';
    return 0;
}