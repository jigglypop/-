#include <cstring>
#include <iostream>

using namespace std;
int A[1000000];
int B[1000000];
void merge(int start, int end)
{
    int mid = (start + end) / 2;
    int left = start;
    int right = mid + 1;
    int i = 0;
    while (left <= mid && right <= end)
        B[i++] = A[left] <= A[right] ? A[left++] : A[right++];
    while (left <= mid)
        B[i++] = A[left++];
    while (right <= end)
        B[i++] = A[right++];
    for (int i = start; i <= end; i++)
        A[i] = B[i - start];
}

void mergesort(int start, int end)
{
    if (start == end)
        return;
    int mid = (start + end) / 2;
    mergesort(start, mid);
    mergesort(mid + 1, end);
    merge(start, end);
}
int main()
{
    freopen("merge_sort.txt", "r", stdin);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int N;
    cin >> N;
    for (int i = 0; i < N; i++)
        cin >> A[i];
    mergesort(0, N - 1);
    for (int i = 0; i < N; i++)
        cout << A[i] << '\n';
    return 0;
}