import sys
sys.stdin = open('2268.txt', 'r')

input = sys.stdin.readline
N, M = map(int, input().split())
board = [0] * (N+1)
tree = [0] * (N+1)


def update(tree, i, x):
    while i < len(tree):
        tree[i] += x
        i += (i & -i)


def sum(tree, i):
    s = 0
    while i > 0:
        s += tree[i]
        i -= (i & -i)
    return s


for _ in range(M):
    a, b, c = map(int, input().split())
    if a == 1:
        update(tree, b, c - board[b])
        board[b] = c
    else:
        X, Y = max(b, c), min(b, c)
        print(sum(tree, X) - sum(tree, Y-1))
