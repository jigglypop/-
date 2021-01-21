#include <iostream>
#include <cstring>
#include <vector>
#include <cstdio>

using namespace std;

// -i = ~i + 1
// L(i) = i & -i

// 펜윅트리 업데이트
void update(vector<long long> &tree, int i, long long diff)
{
    while (i < tree.size())
    {
        tree[i] += diff;
        i += i & -i;
    }
}
// 펜윅트리 합
long long sum(vector<long long> &tree, int i)
{
    long long ans = 0;
    while (i > 0)
    {
        ans += tree[i];
        i -= i & -i;
    }
    return ans;
}

int main()
{
    freopen("fenwick.txt", "r", stdin);
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