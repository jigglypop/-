import sys
from math import log, ceil


def init(tree, board, node, start, end):
    if start == end:
        tree[node] = board[start]
    else:
        init(tree, board, node*2, start, (start+end)//2)
        init(tree, board, node*2+1, (start+end)//2+1, end)
        tree[node] = min(tree[node * 2], tree[node * 2 + 1])


sys.stdin = open("10868.txt", "r")
N, M = map(int, input().split())
H = ceil(log(N, 2))
size = (1 << (H+1))
board = [int(input()) for _ in range(N)]
tree = [0] * size

init(tree, board, 1, 0, N-1)

print(tree)
