#include <iostream>
using namespace std;
int lower_bound(int *arr, int N, int target)
{
    int start = 0;
    int end = N;
    int mid;
    while (end > start)
    {
        mid = (start + end) / 2;
        if (arr[mid] < target)
            start = mid + 1;
        else
            end = mid;
    }
    return end;
}
int main()
{
    //             0  1  2  3  4  5  6  7  8  9
    int arr[10] = {1, 2, 4, 5, 6, 6, 7, 7, 7, 9};
    cout << lower_bound(arr, 10, 7);
    return 0;
}
