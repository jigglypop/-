#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
    //             0  1  2  3  4  5  6  7  8  9
    int arr[10] = {1, 2, 4, 5, 6, 6, 7, 7, 7, 9};
    cout << lower_bound(arr, arr + 10, 7) - arr;
    return 0;
}
