import sys
from math import log, ceil


def init(tree, board, node, start, end):
    if start == end:
        tree[node] = board[start]
    else:
        init(tree, board, node*2, start, (start+end)//2)
        init(tree, board, node*2+1, (start+end)//2+1, end)
        tree[node] = min(tree[node * 2], tree[node * 2 + 1])


def query(tree, node, start, end, i, j):
    if i > end or j < start:
        return -1
    if i <= start and end <= j:
        return tree[node]
    m1 = query(tree, 2*node, start, (start+end)//2, i, j)
    m2 = query(tree, 2*node+1, (start+end)//2+1, end, i, j)
    if m1 == -1:
        return m2
    elif m2 == -1:
        return m1
    else:
        return min(m1, m2)


sys.stdin = open("10868.txt", "r")
N, M = map(int, input().split())
H = ceil(log(N, 2))
size = (1 << (H+1))
board = [int(input()) for _ in range(N)]
tree = [0] * size

init(tree, board, 1, 0, N-1)
for _ in range(M):
    start, end = map(int, input().split())
    print(query(tree, 1, 0, N-1, start-1, end-1))
