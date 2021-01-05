#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;
int main()
{
    freopen("10974.txt", "r", stdin);
    int N;
    scanf("%d", &N);
    vector<int> nums(N);
    for (int i = 1; i <= N; i++)
    {
        nums[i - 1] = i;
    }
    do
    {
        for (int i = 0; i < N; i++)
        {
            printf("%d ", nums[i]);
        }
        printf("\n");
    } while (next_permutation(nums.begin(), nums.end()));
    return 0;
}