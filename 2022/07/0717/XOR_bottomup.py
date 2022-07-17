import sys
sys.stdin = open('./text/12844.txt', 'r')
input = sys.stdin.readline
dp = [i for i in range(10000)]
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()
input = sys.stdin.readline

def lazy_update(i, x):
    tree[i] ^= x * size[i]
    if i < N:
        lazy[i] ^= x

def up(i):
    while i > 1:
        i >>= 1
        tree[i] = tree[2 * i] ^ tree[2 * i + 1]

def down(x):
    for i in reversed(range(1, H + 1)):
        x >>= i
        if lazy[x] != 0:
            lazy_update(2 * x, lazy[x])
            lazy_update(2 * x + 1, lazy[x])
            lazy[x] = 0

def update(l, r, val):
    l += N
    r += N
    l0 = l
    r0 = r
    while l < r:
        if l & 1:
            lazy_update(l, val)
            l += 1
        if r & 1:
            r -= 1
            lazy_update(r, val)
        l >>= 1
        r >>= 1
    up(l0)
    up(r0 - 1)

def query(l, r):
    l += N
    r += N
    down(l)
    down(r - 1)
    res = 0
    while l < r:
        if l & 1:
            res ^= tree[l]
            l += 1
        if r & 1:
            r -= 1
            res ^= tree[r]
        l >>= 1
        r >>= 1
    return res

N = Int()
H = N.bit_length()
tree = [0] * N + List()
lazy = [0] * N
size = [0] * N + [1] * N
for i in reversed(range(1, N)):
    tree[i] = tree[2 * i] ^ tree[2 * i + 1]
    
result = []
for _ in range(Int()):
    temp = List()
    if temp[0] == 1:
        update(temp[1], temp[2] + 1, temp[3])
    else:
        result.append(query(temp[1], temp[2] + 1))
print(*result, sep = "\n")

