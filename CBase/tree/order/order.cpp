#include <cstdio>
#include <iostream>

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
    cout << (char)(x + 'A');
    preorder(tree[x].left);
    preorder(tree[x].right);
}

void inorder(int x)
{
    if (x == -1)
        return;
    inorder(tree[x].left);
    cout << (char)(x + 'A');
    inorder(tree[x].right);
}

void postorder(int x)
{
    if (x == -1)
        return;
    postorder(tree[x].left);
    postorder(tree[x].right);
    cout << (char)(x + 'A');
}

int main()
{
    freopen("order.txt", "r", stdin);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int N;
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        char x, y, z;
        cin >> x >> y >> z;
        x = x - 'A';
        int temp[] = {y, z};
        tree[x].left = y == '.' ? -1 : y - 'A';
        tree[x].right = z == '.' ? -1 : z - 'A';
    }
    preorder(0);
    cout << "\n";
    inorder(0);
    cout << "\n";
    postorder(0);
    cout << "\n";
    return 0;
}