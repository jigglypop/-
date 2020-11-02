from math import ceil, log2
import sys
sys.stdin = open('세그먼트트리.txt', 'r')

input = sys.stdin.readline
N, M = map(int, input().split())
board = [int(input()) for _ in range(N)]
tree = [0] * (1 << (ceil(log2(N)) + 1))


def init(node, start, end):
    if start == end:
        tree[node] = board[start]
    else:
        mid = (start + end) // 2
        init(node * 2, start, mid)
        init(node * 2 + 1, mid + 1, end)
        tree[node] = min(tree[node*2], tree[node*2 + 1])


def query(node, start, end, S, E):
    if end < S or start > E:
        return -1
    if start >= S and end <= E:
        return tree[node]
    mid = (start + end) // 2
    left = query(node * 2, start, mid, S, E)
    right = query(node * 2 + 1, mid+1, end, S, E)
    if left == -1:
        return right
    elif right == -1:
        return left
    else:
        return min(left, right)


init(1, 0, N-1)
for _ in range(M):
    S, E = map(int, input().split())
    print(query(1, 0, N-1, S-1, E-1))
