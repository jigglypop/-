#include <stdio.h>

struct point
{
    int x, y;
    int count;
};

int dx[4] = {0, -1, 0, 1};
int dy[4] = {1, 0, -1, 0};
int main()
{
    int n, m;
    char arr[100][100];
    int visit[10000];
    struct point q[10000];
    struct point *tmp;
    int front, back;
    int num;

    scanf("%d %d", &n, &m);
    num = n * m;
    for (int i = 0; i < n; i++)
        scanf("%s", arr[i]);

    front = 0;
    back = 0;
    q[back].x = 0;
    q[back].y = 0;
    q[back++].count = 1;
    int x, y;
    while (1)
    {
        tmp = &q[front++];
        front %= 10000;
        if (tmp->x == n - 1 && tmp->y == m - 1)
        {
            printf("%d\n", tmp->count);
            return 0;
        }
        for (int i = 0; i < 4; i++)
        {
            x = tmp->x + dx[i];
            y = tmp->y + dy[i];
            if (x >= 0 && x < n && y >= 0 && y < m && arr[x][y] == '1' && visit[x * m + y] == 0)
            {
                visit[x * m + y] = 1;
                q[back].x = x;
                q[back].y = y;
                q[back++].count = tmp->count + 1;
                back %= 10000;
            }
        }
    }
}