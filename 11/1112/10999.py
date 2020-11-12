import sys
sys.stdin = open('10999.txt', 'r')

input = sys.stdin.readline
N, M, K = map(int, input().split())


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


tree = [0] * (N+1)
board = [0]
for i in range(1, N+1):
    board.append(int(input()))
    update(tree, i, board[i])
update(tree, 2, 2)
for _ in range(M+K):
    temp = list(map(int, input().split()))
    if temp[0] == 1:
        for i in range(temp[1], temp[2]+1):
            update(tree, i, temp[3])
    else:
        if temp[1] > 1:
            print(sum(tree, temp[2]) - sum(tree, temp[1]-1))
        else:
            print(sum(tree, temp[2]))
