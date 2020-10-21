#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;
vector<int> nums = {1, 2, 3};
int N = nums.size();
vector<bool> used(N);
int r = 2;

void perm(int k, vector<int> &chosen, vector<bool> &used)
{
    if (k == r)
    {
        for (auto i : chosen)
        {
            printf("%d ", i);
        }
        printf("\n");
        return;
    }

    for (int i = 0; i < N; i++)
    {
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
    return 0;
}