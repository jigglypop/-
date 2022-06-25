import sys
from math import log2
sys.stdin = open("./text/9426.txt", "r")
input = sys.stdin.readline
N, K = map(int, input().split())
P = 65536
tree = [0] * (2 ** (int(log2(P) + 2)))

def update(n, s, e, i, diff):
    tree[n] += diff
    if s == e: return
    elif s <= i <= (s + e)//2:
        update(2 * n, s, (s + e)//2, i, diff)
    else:
        update(2 * n + 1, (s + e)//2+1, e, i, diff)

def query(n, s, e, i):
    if s == e:
        return s
    if tree[2 * n] >= i:
        return query(2 * n, s, (s + e)//2, i)
    else:
        return query(2 * n+1, (s + e)//2+1, e, i-tree[2 * n])

nums = [int(input()) for _ in range(N)]
if K % 2:
    mid = K//2 + 1
else:
    mid = K//2
ans = 0
for i in range(N):
    update(1, 0, P,  nums[i], 1)
    if i >= K:
        update(1, 0, P, nums[i-K], -1)
    if i >= K-1:
        ans += query(1, 0, P, mid)
print(ans)
