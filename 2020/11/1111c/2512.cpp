#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    freopen("2512.txt", "r", stdin);
    int N;
    cin >> N;
    vector<int> A(N);
    for (int i = 0; i < N; i++)
        cin >> A[i];
    int M;
    cin >> M;
    sort(A.begin(), A.end());
    int start = 0;
    int end = A[N - 1];
    int mid;
    int result = 0;
    while (start <= end)
    {
        mid = (start + end) / 2;
        int temp = 0;
        for (auto a : A)
        {
            if (a >= mid)
                temp += mid;
            else
                temp += a;
        }
        if (M >= temp)
            start = mid + 1;
        else
            end = mid - 1;
    }
    cout << end;
    return 0;
}