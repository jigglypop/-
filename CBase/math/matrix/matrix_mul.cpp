#include <cstring>
#include <iostream>
using namespace std;

int A[101][101];
int B[101][101];
int result[101][101];

int main()
{
    freopen("matrix_mul.txt", "r", stdin);
    int Ya, Xa;
    scanf("%d %d", &Ya, &Xa);

    for (int y = 0; y < Ya; y++)
    {
        for (int x = 0; x < Xa; x++)
        {
            scanf("%d ", &A[y][x]);
        }
    }
    int Yb, Xb;
    scanf("%d %d", &Yb, &Xb);
    for (int y = 0; y < Yb; y++)
    {
        for (int x = 0; x < Xb; x++)
        {
            scanf("%d ", &B[y][x]);
        }
    }
    for (int y = 0; y < Ya; y++)
    {
        for (int x = 0; x < Xb; x++)
        {
            for (int z = 0; z < Yb; z++)
            {
                result[y][x] += A[y][z] * B[z][x];
            }
        }
    }
    for (int y = 0; y < Ya; y++)
    {
        for (int x = 0; x < Xb; x++)
        {
            printf("%d ", result[y][x]);
        }
        printf("\n");
    }
    return 0;
}