import sys
sys.stdin = open('2104.txt', 'r')

input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
tree = [0] * (4 * N)

Sum = [0] + A[::]
for i in range(1, len(Sum)):
    Sum[i] += Sum[i-1]


def init(x, s, e):
    if s == e:
        tree[x] = A[s]
        return tree[x]
    mid = (s + e) // 2
    tree[x] = min(init(2 * x, s, mid), init(2 * x + 1, mid+1, e))
    return tree[x]


init(1, 0, N-1)


def query(x, s, e, S, E):
    if S > e or s > E:
        return sys.maxsize
    if S <= s and e <= E:
        return tree[x]
    mid = (s + e) // 2
    return min(query(2 * x, s, mid, S, E), query(2 * x + 1, mid + 1, e, S, E))


print(query(1, 0, N-1, 0, N-1))
