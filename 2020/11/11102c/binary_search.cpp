#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

long long calc(int N)
{
    long long ans = 0;
    for (int start = 1, len = 1; start <= N; start *= 10, len++)
    {
        int end = start * 10 - 1;
        if (end > N)
            end = N;
        ans += (long long)(end - start + 1) * len;
    }
    return ans;
}

int main()
{
    freopen("binary_search.txt", "r", stdin);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int N, K;
    cin >> N >> K;
    cout << N << K;
    return 0;
}