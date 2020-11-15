import sys
sys.stdin = open('1725.txt', 'r')
input = sys.stdin.readline

N = int(input())
board = [int(input()) for _ in range(N)]
tree = [0] * (4 * N)
Max = 0


def init(x, s, e):
    if s == e:
        tree[x] = board[s]
        return tree[x]
    mid = (s + e) // 2
    tree[x] = min(init(2 * x, s, mid), init(2 * x + 1, mid + 1, e))
    return tree[x]


init(1, 0, N-1)


def query(x, s, e, S, E):
    global Max
    print(x, s, e, S, E)
    Max = max(Max, tree[x] * (e - s))
    if S > e or s > E:
        return sys.maxsize
    if S <= s and e <= E:
        return tree[x]
    mid = (s + e) // 2
    return min(query(2 * x, s, mid, S, E), query(2 * x + 1, mid + 1, e, S, E))


query(1, 0, N-1, 0, N-1)
print(Max)
