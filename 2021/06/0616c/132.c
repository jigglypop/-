#include <stdio.h>
#include <string.h>

int doubles(int num)
{
    return num * 2;
}

int main(void)
{
    int num = 1;
    int (*doubles2)(int num);
    doubles2 = doubles;
    int num2 = doubles2(num);
    printf("%d\n", num2);
    return 0;
}