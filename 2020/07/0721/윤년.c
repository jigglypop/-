#include <stdio.h>

int main()
{
    int A, B;
    scanf("%d", &A);
    if ((A % 4 == 0 && A % 100 != 0) || A % 400 == 0)
    {
        B = 1;
    }
    else
    {
        B = 0;
    }
    printf("%d", B);
    return 0;
}