from math import ceil, log2
import sys
sys.stdin = open('세그먼트트리.txt', 'r')

input = sys.stdin.readline
N, M = map(int, input().split())
size = (1 << (ceil(log2(N))+1))
board = [int(input()) for _ in range(N)]
tree = [0] * size


def init(node, start, end):
    if start == end:
        tree[node] = board[start]
    else:
        init(2 * node, start, (start + end) // 2)
        init(2 * node + 1, (start + end) // 2 + 1, end)
        tree[node] = min(tree[node * 2], tree[node * 2 + 1])


init(1, 0, N-1)
print(tree)
