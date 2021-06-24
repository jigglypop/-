#include <stdio.h>

int main(void)
{
    int square[3][3] = {
        {4, 9, 2},
        {3, 5, 7},
        {8, 1, 6}};
    printf("%d\n", square[1][1]);
    printf("%d\n", square[2][1]);
    printf("%d\n", square[0][4]);

    return 0;
}