#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
using namespace std;
long long mod = 127;
long long hashed(string S)
{
    long long ans = 0;
    for (char s : S)
        ans = (ans * 256 + s) % mod;
    return ans;
}
int match(string &S, string &P)
{
    int n = S.length();
    int m = P.length();
    if (n < m)
        return 0;
    long long hashedP = hashed(P);
    long long hashedS = hashed(S.substr(0, m));
    long long first = 1;
    for (int i = 0; i < m - 1; i++)
        first = (first * 256) % mod;
    for (int i = 0; i <= n - m; i++)
    {
        if (hashedP == hashedS)
        {
            if (S.substr(i, m) == P)
                return 1;
        }
        if (i + m < n)
        {
            // 첫자리 빼기
            hashedS = hashedS - (S[i] * first) % mod;
            // 한자리 밀기
            hashedS = (hashedS + mod) % mod;
            // 끝자리 더하기
            hashedS = ((hashedS * 256) % mod + S[i + m]) % mod;
        }
    }
    return 0;
}
int main()
{
    freopen("rabin_karp.txt", "r", stdin);
    string S, P;
    cin >> S >> P;
    cout << match(S, P) << '\n';
    return 0;
}
