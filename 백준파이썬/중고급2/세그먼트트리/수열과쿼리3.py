from bisect import bisect
import sys
from math import ceil, log2
sys.stdin = open('13544.txt', 'r')
input = sys.stdin.readline


def init(x, s, e):
    if s == e:
        tree[x] += [A[s]]
        return tree[x]
    mid = (s + e) // 2
    tree[x] += init(2 * x, s, mid)+init(2 * x + 1, mid + 1, e)
    return tree[x]


def upper(x, s, e, S, E, k):
    if S > e or s > E:
        return 0
    if S <= s and e <= E:
        return len(tree[x]) - bisect(tree[x], k)
    mid = (s + e) // 2
    return upper(2 * x, s, mid, S, E, k)+upper(2 * x + 1, mid + 1, e, S, E, k)


n = int(input())
h = int(ceil(log2(n)))
tree = [[] for _ in range(1 << (h+1))]
A = list(map(int, input().split()))
init(1, 0, n-1)
ans = 0
for i in range(len(tree)):
    tree[i] = sorted(tree[i])
for i in range(int(input())):
    a, b, c = map(int, input().split())
    x, y, z = a ^ ans, b ^ ans, c ^ ans
    ans = upper(1, 0, n-1, x-1, y-1, z)
    print(ans)
