#include <cstdio>
#include <iostream>
#include <vector>


using namespace std;
vector<int> nums = {1, 2, 3, 4, 5, 6, 7, 8};
int N = nums.size();
vector<bool> used(N);
int r = 8;
int count = 0;

void perm(int k, vector<int> &chosen, vector<bool> &used){
    if (k == r){
        // for (auto i : chosen) 
        // if (count == 1) {
        //     for (auto i : chosen) count++;
        // }
        count++;
        return;
    }
    for (int i = 0; i < N; i++){
        if (used[i] == true)
            continue;
        chosen.push_back(nums[i]);
        used[i] = true;
        perm(k + 1, chosen, used);
        chosen.pop_back();
        used[i] = false;
    }
}
int main()
{
    vector<int> chosen;
    perm(0, chosen, used);
    cout << count;
    return 0;
}