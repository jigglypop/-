#include <cstring>
#include <iostream>

using namespace std;
int A[300001];

void quicksort(int start, int end)
{
    if (start >= end)
        return;
    int pivot = (start + end) / 2;
    int left = start;
    int right = end;
    int temp;
    while (left <= right)
    {
        while (A[left] < A[pivot])
            left++;
        while (A[right] > A[pivot])
            right--;
        if (left <= right)
        {
            swap(A[left++], A[right--]);
        }
    }
    quicksort(start, pivot);
    quicksort(pivot + 1, end);
}

int main()
{
    freopen("quick_sort.txt", "r", stdin);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int N;
    cin >> N;
    for (int i = 0; i < N; i++)
        cin >> A[i];
    quicksort(0, N - 1);
    for (int i = 0; i < N; i++)
    {
        cout << A[i] << '\n';
    }
    return 0;
}