#include <stdio.h>

int main()
{
    int N;
    scanf("%d", &N);
    for (int i = 1; i <= N; i++)
    {
        int A, B;
        scanf("%d %d", &A, &B);
        printf("Case #%d: %d\n", i, A + B);
    }
}