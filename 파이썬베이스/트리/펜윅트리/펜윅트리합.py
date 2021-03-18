import sys
sys.stdin = open('펜윅트리합.txt', 'r')


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


input = sys.stdin.readline
n, m, k = map(int, input().split())

tree = [0]*(n+1)
board = [0]
for i in range(1, n+1):
    board.append(int(input()))
    update(tree, i, board[i])
for i in range(0, m+k):
    q, a, b = map(int, input().split())
    if q == 1:
        update(tree, a, b-board[a])
        board[a] = b
    if q == 2:
        print(sum(tree, b) - sum(tree, a-1))
