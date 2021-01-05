#include <stdio.h>
#define num 42
int main()
{
    int a, result = 0;
    int cnt[num] = {
        0,
    };
    for (int i = 0; i < 10; i++)
    {
        scanf("%d\n", &a);
        cnt[a % num]++;
    }
    for (int i = 0; i < num; i++)
    {
        if (cnt[i] != 0)
            result++;
    }
    printf("%d\n", result);
    return 0;
}
