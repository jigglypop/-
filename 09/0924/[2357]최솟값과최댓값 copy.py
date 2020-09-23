import sys
from math import ceil, log2
sys.stdin = open('2357.txt', 'r')

N, M = map(int, input().split())
board = [int(input()) for _ in range(N)]
max_tree = [0 for _ in range(1 << ceil(log2(N))+1)]
min_tree = [0 for _ in range(1 << ceil(log2(N))+1)]


def init(node, start, end):
    if start == end:
        max_tree[node] = board[start]
        min_tree[node] = board[start]
    else:
        mid = (start + end) // 2
        init(2 * node, start, mid)
        init(2 * node + 1, mid + 1, end)
        max_tree[node] = max(max_tree[2 * node], max_tree[2 * node+1])
        min_tree[node] = min(min_tree[2 * node], min_tree[2 * node+1])


init(1, 0, N-1)


def min_query(node, start, end, s, e):
    if s > end or e < start:
        return -1
    if s <= start and e >= end:
        return min_tree[node]
    mid = (start + end) // 2
    left = min_query(2 * node, start, mid, s, e)
    right = min_query(2 * node + 1, mid + 1, end, s, e)
    if left == -1:
        return right
    elif right == -1:
        return left
    else:
        return min(left, right)


def max_query(node, start, end, s, e):
    if s > end or e < start:
        return -1
    if s <= start and e >= end:
        return max_tree[node]
    mid = (start + end) // 2
    left = max_query(2 * node, start, mid, s, e)
    right = max_query(2 * node + 1, mid + 1, end, s, e)
    if left == -1:
        return right
    elif right == -1:
        return left
    else:
        return max(left, right)


for _ in range(M):
    a, b = map(int, input().split())
    print(min_query(1, 0, N-1, a-1, b-1), max_query(1, 0, N-1, a-1, b-1))
