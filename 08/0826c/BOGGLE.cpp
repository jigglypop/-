#include <iostream>
#include <cstring>
#include <algorithm>
#include <stdio.h>
#include <vector>

using namespace std;

char board[5][5];
const int dx[8] = {-1, -1, -1, 1, 1, 1, 0, 0};
const int dy[8] = {-1, 0, 1, -1, 0, 1, -1, 1};

int main()
{
    freopen("BOGGLE.txt", "r", stdin);
    int C;
    cin >> C;
    for (int c = 0; c < C; c++)
    {
        memset(board, 0, sizeof(board));
        for (int y = 0; y < 5; y++)
        {
            for (int x = 0; x < 5; x++)
            {
                cin >> board[y][x];
                cout << board[y][x] << "\t";
            }
            cout << endl;
        }
    }
    return 0;
}