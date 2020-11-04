#include <iostream>
#include <cstring>
#include <vector>

using namespace std;
void update(vector<int> &tree, int i, int diff)
{
    while (i < tree.size())
    {
        tree[i] += diff;
        i += i & -i;
    }
}

long long sum(vector<int> &tree, int i)
{
    long long result = 0;
    while (i > 0)
    {
        result += tree[i];
        i -= i & -i;
    }
    return result;
}

int main()
{
    freopen("11659.txt", "r", stdin);
    int N, M;
    scanf("%d %d", &N, &M);
    vector<int> A(N + 1);
    vector<int> tree(N + 1);
    for (int i = 1; i <= N; i++)
    {
        scanf("%d ", &A[i]);
        update(tree, i, A[i]);
    }
    for (int i = 0; i < M; i++)
    {
        int a, b;
        scanf("%d %d", &a, &b);
        printf("%lld\n", sum(tree, b) - sum(tree, a - 1));
    }
    return 0;
}