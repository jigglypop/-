#include <iostream>
#include <cstring>
#include <vector>
using namespace std;
const long long mod = 1000000LL;
typedef vector<vector<long long>> matrix;

matrix operator*(const matrix &a, const matrix &b)
{
    int n = a.size();
    matrix c(n, vector<long long>(n));
    for (int y = 0; y < n; y++)
    {
        for (int x = 0; x < n; x++)
        {
            for (int k = 0; k < n; k++)
                c[y][x] += a[y][k] * b[k][x];
            c[y][x] %= mod;
        }
    }
    return c;
}

int main()
{
    freopen("matrix.txt", "r", stdin);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    long long N;
    cin >> N;
    if (N <= 1)
    {
        cout << N << "\n";
        return 0;
    }
    N -= 1;
    matrix ans = {{1, 0}, {0, 1}};
    matrix x = {{1, 1}, {1, 0}};
    while (N > 0)
    {
        if (N % 2 == 1)
            ans = ans * x;
        x = x * x;
        N /= 2;
    }
    cout << ans[0][0] << "\n";
    return 0;
}