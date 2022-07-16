
import sys
sys.setrecursionlimit(10 ** 5)
sys.stdin = open('./text/14428.txt', 'r')
input = sys.stdin.readline
dp = [i for i in range(10000)]
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()
def Min(A, B):return min(sorted([A, B]), key=lambda x: board[x])

N = Int()
board = [0] + List()
tree = [0 for _ in range(N)] + [i for i in range(1, N + 1)]
for i in reversed(range(1, N)):
    tree[i] = Min(tree[2 * i], tree[2 * i ^ 1])

def query(l, r):
    l += N - 1
    r += N - 1
    res = tree[l]
    while l <= r:
        if l % 2 == 1:
            res = Min(res, tree[l])
            l += 1
        if r % 2 == 0:
            res = Min(res, tree[r])
            r -= 1
        l //= 2
        r //= 2
    return res


def update(i, x):
    board[i] = x
    i += N - 1
    while i > 1:
        tree[i // 2] = Min(tree[i], tree[i ^ 1])
        i //= 2

for _ in range(Int()):
    a, b, c = Split()
    if a == 1:
        update(b, c)
    else:
        print(query(b, c))

