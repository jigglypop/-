#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
    freopen("sort_pair.txt", "r", stdin);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int N;
    cin >> N;
    vector<pair<int, int>> A(N);
    for (int i = 0; i < N; i++)
        cin >> A[i].first >> A[i].second;
    sort(A.begin(), A.end());
    for (int i = 0; i < A.size(); i++)
        cout << A[i].first << ' ' << A[i].second << '\n';
    return 0;
}