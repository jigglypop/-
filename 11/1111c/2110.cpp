#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;
int main()
{
    freopen("2110.txt", "r", stdin);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int N, K;
    cin >> N >> K;
    vector<long long> A(N);
    for (int i = 0; i < N; i++)
        cin >> A[i];
    sort(A.begin(), A.end());
    int start = 1;
    int end = A[N - 1] - A[0];
    int mid;
    int result = 1;
    while (start <= end)
    {
        mid = (start + end) / 2;
        long long idx = 0;
        long long count = 1;
        for (int i = 1; i < N; i++)
        {
            if (A[idx] + mid <= A[i])
            {
                count += 1;
                idx = i;
            }
        }
        if (count >= K)
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