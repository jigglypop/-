from math import ceil, log2
import sys
sys.stdin = open('세그먼트트리.txt', 'r')

input = sys.stdin.readline
N, M = map(int, input().split())
board = [int(input()) for _ in range(N)]
tree = [0] * (1 << ceil(log2(N))+1)


def init(node, start, end):
    if start == end:
        tree[node] = board[start]
    else:
        mid = (start + end) // 2
        init(2 * node, start,  mid)
        init(2 * node + 1, mid + 1, end)
        tree[node] = max(tree[2 * node], tree[2 * node + 1])


init(1, 0, N-1)
print(tree)


def query(node, start, end, s, e):
    if s > end or e < start:
        return -1
    if s <= start and end <= e:
        return tree[node]
    mid = (start + end) // 2
    left = query(2 * node, start, mid, s, e)
    right = query(2 * node + 1, mid + 1, end, s, e)
    if left == -1:
        return right
    elif right == -1:
        return left
    else:
        return max(left, right)


for _ in range(M):
    start, end = map(int, input().split())
    print(query(1, 0, N-1, start-1, end-1))
