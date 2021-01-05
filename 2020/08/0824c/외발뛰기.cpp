#include <iostream>
#include <string.h>
using namespace std;

int map[101][101];
int check[101][101];
int n;
int jump(int x, int y)
{
    if (x >= n || y >= n)
    {
        return 0;
    }
    if (x == n - 1 && y == n - 1)
    {
        return 1;
    }

    if (check[x][y] != -1)
    {
        return check[x][y];
    }

    check[x][y] = (jump(x + map[x][y], y) || jump(x, y + map[x][y]));

    return check[x][y];
}
int main()
{
    // freopen("./외발뛰기.txt", "r", stdin);
    int tc;
    cin >> tc;

    for (int t = 1; t <= tc; t++)
    {
        memset(check, -1, sizeof(check));
        memset(map, -1, sizeof(map));

        cin >> n;

        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                cin >> map[i][j];
            }
        }

        int c = jump(0, 0);

        if (c == 1)
        {
            cout << "YES" << endl;
        }
        else
        {
            cout << "NO" << endl;
        }
    }

    return 0;
}
