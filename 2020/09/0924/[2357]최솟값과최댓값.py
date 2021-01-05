import sys
from math import ceil, log2
sys.stdin = open('2357.txt', 'r')

N, M = map(int, input().split())
board = [int(input()) for _ in range(N)]
tree = [[0, 0] for _ in range(1 << ceil(log2(N))+1)]


def init(node, start, end):
    if start == end:
        tree[node][0] = board[start]
        tree[node][1] = board[start]
    else:
        mid = (start + end) // 2
        init(2 * node, start, mid)
        init(2 * node + 1, mid + 1, end)
        tree[node][0] = min(tree[2 * node][0], tree[2 * node+1][0])
        tree[node][1] = max(tree[2 * node][1], tree[2 * node+1][1])


init(1, 0, N-1)


def query(node, start, end, s, e):
    if s > end or e < start:
        return -1
    if s <= start and e >= end:
        return tree[node][0], tree[node][1]
    mid = (start + end) // 2
    left = query(2 * node, start, mid, s, e)
    right = query(2 * node + 1, mid + 1, end, s, e)
    if left == -1:
        return right
    elif right == -1:
        return left
    else:
        return min(left, right), max(left, right)


for _ in range(M):
    a, b = map(int, input().split())
    print(query(1, 0, N-1, a-1, b-1))
