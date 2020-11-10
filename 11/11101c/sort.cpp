#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    freopen("quick_sort.txt", "r", stdin);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int N;
    cin >> N;
    vector<int> A(N);
    for (int i = 0; i < N; i++)
        cin >> A[i];
    sort(A.begin(), A.end());
    for (int i = 0; i < N; i++)
        cout << A[i] << "\n";
    return 0;
}