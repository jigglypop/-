#include <cstdio>
#include <algorithm>
#define left _left
#define right _right
using namespace std;
struct Node
{
    int left, right;
    int order, depth;
};
Node tree[10001];
int left[10001];
int right[10001];
int cnt[10001];
int order = 0;

void inorder(int x, int depth)
{
    if (x == -1)
        return;
    inorder(tree[x].left, depth + 1);
    tree[x].order = ++order;
    tree[x].depth = depth;
    inorder(tree[x].right, depth + 1);
}

int main()
{
    freopen("./2250.txt", "r", stdin);
    int N;
    scanf("%d", &N);
    for (int i = 0; i < N; i++)
    {
        int a, b, c;
        scanf("%d %d %d", &a, &b, &c);
        tree[a].left = b;
        tree[a].right = c;
        if (b != -1)
            cnt[b]++;
        if (c != -1)
            cnt[c]++;
    }
    int root = 0;
    for (int i = 1; i <= N; i++)
    {
        if (cnt[i] == 0)
        {
            root = i;
        }
    }
    inorder(root, 1);
    int maxdepth = 0;
    for (int i = 1; i <= N; i++)
    {
        int depth = tree[i].depth;
        int order = tree[i].order;
        if (left[depth] == 0)
        {
            left[depth] = order;
        }
        else
        {
            left[depth] = min(left[depth], order);
        }
        right[depth] = max(right[depth], order);
        maxdepth = max(maxdepth, depth);
    }
    int ans = 0;
    int ans_level = 0;
    for (int i = 1; i <= maxdepth; i++)
    {
        if (ans < right[i] - left[i] + 1)
        {
            ans = right[i] - left[i] + 1;
            ans_level = i;
        }
    }
    printf("%d %d\n", ans_level, ans);
    return 0;
}