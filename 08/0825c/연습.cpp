#include <iostream>
using namespace std;
int main()
{
    // freopen("input.txt", "r", stdin);
    int Y = 5;
    int X = 5;
    int board[Y][X];
    for (int y = 0; y < Y; y++)
    {
        for (int x = 0; x < X; x++)
        {
            board[y][x] = y * x;
        }
    }

    for (int y = 1; y < Y; y++)
    {
        for (int x = 1; x < X; x++)
        {
            cout << board[y][x] << "\t";
        }
        cout << '\n';
    }
    return 0;
}
