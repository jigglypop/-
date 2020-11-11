#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
    freopen("2110.txt", "r", stdin);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int N, C;
    cin >> N >> C;
    vector<int> router(N);
    for (int i = 0; i < N; i++)
        cin >> router[i];
    sort(router.begin(), router.end());
    int start = 1;
    int end = router[N - 1] - router[0];
    int mid;
    int result = 0;
    while (start <= end)
    {
        mid = (start + end) / 2;
        int idx = 0;
        int count = 1;
        for (int i = 1; i < N; i++)
        {
            if (router[i] - router[idx] >= mid)
            {
                count++;
                idx = i;
            }
        }
        if (C <= count)
        {
            result = mid;
            start = mid + 1;
        }
        else
            end = mid - 1;
    }
    cout << result;
    return 0;
}