
import sys
sys.stdin = open('./text/12844.txt', 'r')
input = sys.stdin.readline
dp = [i for i in range(10000)]
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()
input = sys.stdin.readline

def init(x, s, e):
    if s == e:
        tree[x] = board[s]
        return tree[x]
    mid = (s + e) // 2
    tree[x] = init(2 * x, s, mid) ^ init(2 * x + 1, mid + 1, e)
    return tree[x]

def update(x, s, e, S, E, diff):
    if lazy[x] != 0:
        L = (e - s + 1)
        if L % 2 == 1:
            tree[x] ^= lazy[x]
        if s != e:
            lazy[2 * x] ^= lazy[x]
            lazy[2 * x + 1] ^= lazy[x]
        lazy[x] = 0
    if S > e or s > E:
        return
    if S <= s and e <= E:
        L = (e - s + 1)
        if L % 2 == 1:
            tree[x] ^= diff
        if s != e:
            lazy[2 * x] ^= diff
            lazy[2 * x + 1] ^= diff
        return
    mid = (s + e) // 2
    update(2 * x, s, mid, S, E, diff)
    update(2 * x + 1, mid + 1, e, S, E, diff)
    tree[x] = tree[2 * x] ^ tree[2 * x + 1]


def query(x, s, e, S, E):
    if lazy[x] != 0:
        L = (e - s + 1)
        if L % 2 == 1:
            tree[x] ^= lazy[x]
        if s != e:
            lazy[2 * x] ^= lazy[x]
            lazy[2 * x + 1] ^= lazy[x]
        lazy[x] = 0
    if S > e or s > E:
        return 0
    if S <= s and e <= E:
        return tree[x]
    mid = (s + e) // 2
    return query(2 * x, s, mid, S, E) ^ query(2 * x + 1, mid + 1, e, S, E)

N = Int()
board = List()
tree = [0] * (4 * N)
lazy = [0] * (4 * N)
init(1, 0, N - 1)
for _ in range(Int()):
    temp = List()
    if temp[0] == 1:
        a, b, c, d = temp
        update(1, 0, N-1, min(b, c), max(b, c), d)
    else:
        a, b, c = temp
        print(query(1, 0, N-1, min(b, c), max(b, c)))