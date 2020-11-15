import sys
from math import log2, ceil
sys.stdin = open('1725.txt', 'r')
input = sys.stdin.readline

N = int(input())
board = [int(input()) for _ in range(N)]
tree = [0] * (1 << ceil(log2(N)+1))
start = [0] * (1 << ceil(log2(N)+1))
end = [0] * (1 << ceil(log2(N)+1))


def init(x, s, e):
    if s == e:
        tree[x] = board[s]
        return tree[x]
    mid = (s + e) // 2
    tree[x] = min(init(2 * x, s, mid), init(2 * x + 1, mid + 1, e))
    start[x] = s
    end[x] = e
    return tree[x]


init(1, 0, N-1)


def query(x, s, e, S, E):
    if S > e or s > E:
        return sys.maxsize
    if S <= s and e <= E:
        return tree[x]
    mid = (s + e) // 2
    return min(query(2 * x, s, mid, S, E), query(2 * x + 1, mid + 1, e, S, E))


query(1, 0, N-1, 0, N-1)
Max = 0
for i in range(1, len(tree)):
    Max = max(Max, tree[i] * (end[i] - start[i] + 1))
print(Max)
