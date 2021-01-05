#include <cstdio>
#include <vector>
using namespace std;

bool next_perm(vector<int> &nums, int N)
{
    int i = N - 1;
    while (i > 0 && nums[i - 1] >= nums[i])
    {
        i -= 1;
    }
    if (i <= 0)
    {
        return false;
    }
    int j = N - 1;
    while (nums[j] <= nums[i - 1])
    {
        j -= 1;
    }
    swap(nums[i - 1], nums[j]);
    j = N - 1;
    while (i < j)
    {
        swap(nums[i], nums[j]);
        i += 1;
        j -= 1;
    }
    return true;
}

int main()
{
    freopen("10972.txt", "r", stdin);
    int N;
    scanf("%d", &N);
    vector<int> nums(N);
    for (int i = 0; i < N; i++)
    {
        scanf("%1d ", &nums[i]);
    }

    if (next_perm(nums, N))
    {
        for (int i = 0; i < N; i++)
        {
            printf("%d ", nums[i]);
        }
    }
    else
    {
        puts("-1");
    }
    return 0;
}