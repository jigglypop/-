#include <cstdio>

using namespace std;
struct Node
{
    int left;
    int right;
};
Node tree[50];

void preorder(int x)
{
    if (x == -1)
        return;
    printf("%c", x + 'A');
    preorder(tree[x].left);
    preorder(tree[x].right);
}

void inorder(int x)
{
    if (x == -1)
        return;
    inorder(tree[x].left);
    printf("%c", x + 'A');
    inorder(tree[x].right);
}

void postorder(int x)
{
    if (x == -1)
        return;
    postorder(tree[x].left);
    postorder(tree[x].right);
    printf("%c", x + 'A');
}

int main()
{
    freopen("./order.txt", "r", stdin);
    int N;
    scanf("%d\n", &N);
    for (int i = 0; i < N; i++)
    {
        char x, y, z;
        scanf("%c %c %c\n", &x, &y, &z);
        x = x - 'A';
        if (y == '.')
        {
            tree[x].left = -1;
        }
        else
        {
            tree[x].left = y - 'A';
        }
        if (z == '.')
        {
            tree[x].right = -1;
        }
        else
        {
            tree[x].right = z - 'A';
        }
    }
    preorder(0);
    puts("");
    inorder(0);
    puts("");
    postorder(0);
    puts("");
    return 0;
}