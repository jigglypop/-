#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;
int nums[4];

int main() {
    freopen("2752.txt", "r", stdin);
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    for (int i = 0; i < 3;i++){
        cin >> nums[i];
    }
    sort(nums, nums + 3);
    for (int i = 0; i < 3;i++){
        cout << nums[i] << " ";
    }
    return 0;
}
