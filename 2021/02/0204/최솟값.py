import sys
sys.stdin = open('10868.txt', 'r')

N, M = map(int, input().split())
board = [int(input()) for _ in range(N)]
tree = [0] * (4 * N)


def init(x, s, e):
    if s == e:
        tree[x] = board[e]
        return tree[x]
    mid = (s + e) // 2
    tree[x] = min(init(2 * x, s, mid), init(2 * x + 1, mid + 1, e))
    return tree[x]


init(1, 0, N-1)


def query(x, s, e, S, E):
    if S > e or s > E:
        return sys.maxsize
    if S <= s and e <= E:
        return tree[x]
    mid = (s + e) // 2
    return min(query(2 * x, s, mid, S, E), query(2 * x + 1, mid + 1, e, S, E))


for _ in range(M):
    s, e = map(int, input().split())
    print(query(1, 0, N-1, s-1, e-1))
