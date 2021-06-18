#include <stdio.h>

void print_arr(int *arr[2])
{
    printf("%d %d ", *arr[0], *arr[1]);
}

int main(void)
{
    int x = 5, y = 10;
    int *arr[2];
    arr[0] = &x;
    arr[1] = &y;
    print_arr(arr);
    return 0;
}