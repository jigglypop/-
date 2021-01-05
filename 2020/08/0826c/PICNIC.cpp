#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <cstring>

using namespace std;

int ans;
int N, M;
bool areFriends[10][10];
bool taken[10];

void counting(int n)
{
    bool finished = true;
    int first = -1;
    for (int i = 0; i < N; i++)
    {
        if (!taken[i])
        {
            finished = false;
            first = i;
            break;
        }
    }

    if (finished)
    {
        ans++;
        return;
    }

    for (int j = first + 1; j < N; j++)
    {
        if (!taken[first] && !taken[j] && areFriends[first][j])
        {
            taken[first] = true;
            taken[j] = true;
            counting(n + 1);
            taken[first] = false;
            taken[j] = false;
        }
    }

    return;
}

int main()
{
    // freopen("PICNIC.txt", "r", stdin);
    int tc;
    cin >> tc;

    for (int t = 1; t <= tc; t++)
    {
        ans = 0;
        memset(taken, false, sizeof(taken));
        memset(areFriends, false, sizeof(areFriends));

        cin >> N >> M;

        for (int i = 0; i < M; i++)
        {
            int a, b;
            cin >> a >> b;
            areFriends[a][b] = true;
            areFriends[b][a] = true;
        }

        counting(0);
        cout << ans << endl;
    }

    return 0;
}
