#include <iostream>
using namespace std;

int post[100000];
int inorder_idx[100001];
void preorder(int is, int ie, int ps, int pe)
{
    if (is > ie || ps > pe)
        return;
    int root = post[pe];
    cout << root << " ";
    preorder(is, inorder_idx[root] - 1, ps, ps + inorder_idx[root] - is - 1);
    preorder(inorder_idx[root] + 1, ie, ps + inorder_idx[root] - is, pe - 1);
}
int main()
{
    freopen("printpreorder.txt", "r", stdin);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int n;
    cin >> n;
    for (int i = 0, in; i < n; i++)
    {
        cin >> in;
        inorder_idx[in] = i;
    }
    for (int i = 0; i < n; i++)
        cin >> post[i];
    preorder(0, n - 1, 0, n - 1);
    return 0;
}