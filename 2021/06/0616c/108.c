#include <stdio.h>

int main(void)
{
    int x = 0, y = 0;
    int *arr[11];
    arr[0] = &x;
    arr[1] = &y;
    printf("%d %d\n", *arr[0], *arr[1]);
    *arr[0] = 10;
    *arr[1] = 20;
    printf("%d %d\n", *arr[0], *arr[1]);
    return 0;
}