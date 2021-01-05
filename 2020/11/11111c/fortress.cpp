#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int C, N, longest;
int x[101], y[101], radius[101];
struct Tree
{
    vector<Tree *> children;
};
bool enclose(int a, int b)
{
    if (radius[a] > radius[b])
    {
        int dx = x[a] - x[b], dy = y[a] - y[b];
        if (pow(dx, 2) + pow(dy, 2) < pow(radius[a] - radius[b], 2))
            return true;
    }
    return false;
}

bool isChild(int parent, int child)
{
    if (!enclose(parent, child))
        return false;
    for (int i = 0; i < N; i++)
    {
        if (i != parent && i != child && enclose(parent, i) && enclose(i, child))
            return false;
    }
    return true;
}

Tree *getTree(int root)
{
    Tree *temp = new Tree();
    for (int i = 0; i < N; i++)
    {
        if (isChild(root, i))
            temp->children.push_back(getTree(i));
    }
    return temp;
}

int height(Tree *root)
{
    vector<int> heights;
    for (int i = 0; i < root->children.size(); i++)
        heights.push_back(height(root->children[i]));
    if (heights.empty())
        return 0;
    sort(heights.begin(), heights.end());
    if (heights.size() >= 2)
        longest = max(longest, 2 + heights[heights.size() - 2] + heights[heights.size() - 1]);
    return heights.back() + 1;
}

int solve(Tree *root)
{
    longest = 0;
    int h = height(root);
    return max(longest, h);
}

int main()
{
    freopen("fortress.txt", "r", stdin);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> C;
    while (C--)
    {
        cin >> N;
        for (int i = 0; i < N; i++)
            cin >> x[i] >> y[i] >> radius[i];
        Tree *T = getTree(0);
        cout << solve(T) << endl;
    }
    return 0;
}
