#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
int parent[1000001];
int Find(int x)
{
    if (parent[x] != x)
        parent[x] = Find(parent[x]);
    return parent[x];
}
void Union(int x, int y)
{
    x = Find(x);
    y = Find(y);
    if (parent[x] < parent[y])
        swap(x, y);
    parent[y] = x;
}
int main()
{
    freopen("1717.txt", "r", stdin);
    int n, m;
    cin >> n >> m;
    for (int i = 0; i <= n; i++)
    {
        parent[i] = i;
    }
    while (m--)
    {
        int w, x, y;
        cin >> w >> x >> y;
        if (w == 0)
        {
            Union(x, y);
        }
        else
        {
            x = Find(x);
            y = Find(y);
            if (x == y)
            {
                cout << "YES" << '\n';
            }
            else
            {
                cout << "NO" << '\n';
            }
        }
    }
    for (auto i : parent)
    {
        if (i != 0)
            cout << i << " ";
    }
}