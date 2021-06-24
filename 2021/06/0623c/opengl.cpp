#include <iostream>

void draw1(int h)
{
    if (h == 0)
    {
        return;
    }
    draw1(h - 1);
    for (int i = 0; i < h; i++)
    {
        printf("*");
    }
    printf("\n");
}
void draw2(int h)
{
    for (int o = 0; o < h; o++)
    {
        for (int i = 0; i < o; i++)
        {
            printf("*");
        }
        printf("\n");
    }
}
int main(void)
{
    draw1(5);
    draw2(5);
    return 0;
}