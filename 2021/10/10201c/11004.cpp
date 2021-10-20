#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
int N, K;
int nums[5000002];
int main() {
    freopen("11004.txt", "r", stdin);
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    cin >> N >> K;
    for (int i = 0; i < N;i++){
        cin >> nums[i];
    }
    sort(nums, nums + N);
    cout << nums[K - 1];
    return 0;
}