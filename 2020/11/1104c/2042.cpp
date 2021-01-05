#include <iostream>
#include <cstring>
#include <vector>
#include <cstdio>

using namespace std;

// 펜윅트리 업데이트
void update(vector<long long> &tree, int x, long long diff)
{
    for (int i = x; i < tree.size(); i += i & -i)
    {
        tree[i] += diff;
    }
}
// 펜윅트리 합
long long sum(vector<long long> &tree, int x)
{
    long long ans = 0;
    for (int i = x; i > 0; i -= i & -i)
    {
        ans += tree[i];
    }
    return ans;
}

int main()
{
    freopen("2042.txt", "r", stdin);
    int N, M, K;
    scanf("%d %d %d", &N, &M, &K);
    vector<long long> A(N + 1);
    vector<long long> tree(N + 1);
    for (int i = 1; i <= N; i++)
    {
        scanf("%lld", &A[i]);
        update(tree, i, A[i]);
    }
    M += K;
    while (M--)
    {
        int a;
        scanf("%d", &a);
        if (a == 1)
        {
            int b;
            long long c;
            scanf("%d %lld", &b, &c);
            long long diff = c - A[b];
            A[b] = c;
            update(tree, b, diff);
        }
        else
        {
            int b, c;
            scanf("%d %d", &b, &c);
            printf("%lld\n", sum(tree, c) - sum(tree, b - 1));
        }
    }
    return 0;
}