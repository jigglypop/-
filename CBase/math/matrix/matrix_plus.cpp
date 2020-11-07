#include <cstring>
#include <iostream>
using namespace std;

int result[101][101];

int main()
{
    freopen("matrix_plus.txt", "r", stdin);
    int Y, X;
    scanf("%d %d", &Y, &X);
    for (int k = 0; k < 2; k++)
    {
        for (int y = 0; y < Y; y++)
        {
            for (int x = 0; x < X; x++)
            {
                int temp;
                scanf("%d ", &temp);
                result[y][x] += temp;
            }
        }
    }
    for (int y = 0; y < Y; y++)
    {
        for (int x = 0; x < X; x++)
        {
            printf("%d ", result[y][x]);
        }
        printf("\n");
    }
    return 0;
}