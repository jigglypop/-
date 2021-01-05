#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
long long a[1000000];

int main()
{
    freopen("binary_search_lowerbound.txt", "r", stdin);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int n;
    long long m;
    scanf("%d %lld", &n, &m);
    long long l = 0;
    long long r = 0;
    for (int i = 0; i < n; i++)
    {
        scanf("%lld", &a[i]);
        if (r < a[i])
        {
            r = a[i];
        }
    }
    long long ans = 0;
    while (l <= r)
    {
        long long mid = (l + r) / 2;
        long long sum = 0;
        for (int i = 0; i < n; i++)
        {
            if (a[i] - mid > 0)
                sum += a[i] - mid;
        }
        if (sum >= m)
        {
            if (ans < mid)
                ans = mid;
            l = mid + 1;
        }
        else
            r = mid - 1;
    }
    printf("%lld\n", ans);
    return 0;
}