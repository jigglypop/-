#include <stdio.h>

void changeA(int x1);
void changeB(int *x2);

int main()
{
    int x = 10;
    changeA(x);
    printf("%d\n", x);
    changeB(&x);
    printf("%d\n", x);
    return 0;
}
void changeA(int x1)
{
    x1 = 20;
};
void changeB(int *x2)
{
    *x2 = 40;
};