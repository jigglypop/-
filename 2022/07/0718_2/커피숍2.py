import sys
sys.stdin = open('./text/2252.txt', 'r')
input = sys.stdin.readline
dp = [i for i in range(10000)]
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()
N, Q = Split()
board = [0] + List()
tree = [0] * (N + 1)

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
    x, y, a, b = Split()
    X, Y = max(x, y), min(x, y)
    if Y > 1:
        print(sum(tree, X) - sum(tree, Y-1))
    else:
        print(sum(tree, X))
    update(tree, a, b - board[a])
    board[a] = b

