#include <stdio.h>
#include <stdlib.h>

int main()
{
    int *stk;
    stk = calloc(10, sizeof(int));
    stk[0] = 1;
    printf("%d", stk[10]);
    return 0;
}