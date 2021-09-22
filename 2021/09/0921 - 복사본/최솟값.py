import sys
sys.stdin = open('10868.txt', 'r')
input = sys.stdin.readline
N, M = map(int, input().split())
tree = [0] * N + [int(input()) for _ in range(N)]

for i in reversed(range(N)):
    tree[i] = min(tree[2 * i], tree[2 * i ^ 1])

for _ in range(M):
    l, r = map(int, input().split())
    l += N - 1
    r += N - 1 
    Min = sys.maxsize
    while l <= r:
        if l % 2:
            Min = min(Min, tree[l])
            l += 1
        if not (r % 2):
            Min = min(Min, tree[r])
            r -= 1
        r >>= 1
        l >>= 1
    print(Min)