# from math import ceil, log2
import sys
# 10868
sys.stdin = open('세그먼트트리.txt', 'r')

input = sys.stdin.readline
N, M = map(int, input().split())
# size = (1 << (ceil(log2(N))+1))
board = [int(input()) for _ in range(N)]
tree = [0] * (4*N)


def init(x, start, end):
    if start == end:
        tree[x] = board[end]
    else:
        init(2 * x, start, (start + end) // 2)
        init(2 * x + 1, (start + end) // 2 + 1, end)
        tree[x] = min(tree[x * 2], tree[x * 2 + 1])


init(1, 0, N-1)


def query(x, start, end, s, e):
    if end < s or start > e:
        return -1
    if start >= s and end <= e:
        return tree[x]
    mid = (start + end) // 2
    left = query(2 * x, start, mid, s, e)
    right = query(2 * x + 1, mid + 1, end, s, e)
    if left == -1:
        return right
    elif right == -1:
        return left
    else:
        return min(left, right)


for _ in range(M):
    start, end = map(int, input().split())
    print(query(1, 0, N-1, start-1, end-1))
