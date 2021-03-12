import sys
sys.stdin = open('10999.txt', 'r')
input = sys.stdin.readline
n, m, k = map(int, input().split())
board = [int(input()) for i in range(n)]
tree = [0] * (4 * n)
lazy = [0] * (4 * n)


def init(x, s, e):
    if s == e:
        tree[x] = board[s]
        return tree[x]
    mid = (s+e) // 2
    tree[x] = init(2 * x, s, mid) + init(2 * x + 1, mid + 1, e)
    return tree[x]


def update_lazy(x, s, e):
    if lazy[x] == 0:
        return
    tree[x] += (e - s + 1) * lazy[x]
    if s != e:
        lazy[2 * x] += lazy[x]
        lazy[2 * x + 1] += lazy[x]
    lazy[x] = 0


def update(x, s, e, S, E, diff):
    update_lazy(x, s, e)
    if S > e or s > E:
        return
    if S <= s and e <= E:
        tree[x] += (e - s + 1) * diff
        if s != e:
            lazy[2 * x] += diff
            lazy[2 * x + 1] += diff
        return
    mid = (s + e)//2
    update(2 * x, s, mid, S, E, diff)
    update(2 * x + 1, mid + 1, e, S, E, diff)
    tree[x] = tree[2 * x] + tree[2 * x + 1]


def query(x, s, e, S, E):
    update_lazy(x, s, e)
    if S > e or s > E:
        return 0
    if S <= s and e <= E:
        return tree[x]
    mid = (s + e)//2
    return query(2 * x, s, mid, S, E) + query(2 * x + 1, mid + 1, e, S, E)


init(1, 0, n-1)
for i in range(m+k):
    temp = list(map(int, input().split()))
    if temp[0] == 1:
        a, b, c, d = temp
        update(1, 0, n-1, b-1, c-1, d)
    else:
        a, b, c = temp
        print(query(1, 0, n-1, b-1, c-1))
