#include <stdio.h>

int main(void)
{

    int input, index, max;
    int arr[9];
    for (int i = 0; i < 9; i++)
    {
        scanf("%d", &input);
        arr[i] = input;
    }
    index = 1;
    max = arr[0];
    for (int i = 0; i < 9; i++)
    {
        if (max < arr[i])
        {
            max = arr[i];
            index = (int)i + 1;
        }
    }
    printf("%d\n%d", max, index);
}