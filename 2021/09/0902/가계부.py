import sys
sys.stdin = open('12837.txt', 'r')
N, Q = map(int, input().split())
tree = [0] * (N + 1)


def update(i, x):
    while i < len(tree):
        tree[i] += x
        i += (i & -i)


def sum(i):
    s = 0
    while i > 0:
        s += tree[i]
        i -= (i & -i)
    return s


for _ in range(Q):
    q, a, b = map(int, input().split())
    if q == 1:
        update(a, b)
    else:
        print(sum(b) - sum(a-1))
