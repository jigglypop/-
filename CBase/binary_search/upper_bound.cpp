#include <iostream>
using namespace std;
int upper_bound(int *arr, int N, int target)
{
    int start = 0;
    int end = N - 1;
    int mid;
    int result = 0;
    while (start < end)
    {
        mid = (start + end) / 2;
        if (arr[mid] <= target)
            start = mid + 1;
        else
            end = mid;
    }
    return start;
}
int main()
{
    //             0  1  2  3  4  5  6  7  8  9
    int arr[10] = {1, 2, 4, 5, 6, 6, 7, 7, 7, 9};
    cout << upper_bound(arr, 10, 7);
    return 0;
}
