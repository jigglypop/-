#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;
vector<int> nums = {1, 2, 3};
int N = nums.size();
int r = 2;

void comb(int k, vector<int> &chosen, int start)
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

    for (int i = start; i < N; i++)
    {

        chosen.push_back(nums[i]);
        comb(k + 1, chosen, i + 1);
        chosen.pop_back();
    }
}

int main()
{
    vector<int> chosen;
    comb(0, chosen, 0);
    return 0;
}