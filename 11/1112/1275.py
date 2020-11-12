import sys
sys.stdin = open('1275.txt', 'r')

input = sys.stdin.readline
N, Q = map(int, input().split())
board = [0] + list(map(int, input().split()))
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


for i in range(1, N+1):
    update(tree, i, board[i])

for _ in range(Q):
    x, y, a, b = map(int, input().split())
    X, Y = max(x, y), min(x, y)
    if Y > 1:
        print(sum(tree, X) - sum(tree, Y-1))
    else:
        print(sum(tree, X))
    update(tree, a, b-board[a])
    board[a] = b
