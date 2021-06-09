import sys
sys.stdin = open("2243.txt", "r")
input = sys.stdin.readline
N = int(input())
# MAX = 1000001
MAX = 6
tree = [0] * (2 * MAX)


def update(i, x):
    tree[i] += x
    while i > 1:
        tree[i // 2] = tree[i] + tree[i ^ 1]
        i //= 2


def query(l, r, n):
    res = 0
    while l <= r:
        if l % 2:
            res += tree[l]
            l += 1
        if not (r % 2):
            res += tree[r]
            r -= 1
        l >>= 1
        r >>= 1
    # if l == r:
    #     res += tree[r]
    return res


for _ in range(N):
    temp = list(map(int, input().split()))
    if temp[0] == 2:
        a, b = temp[1] + MAX, temp[2]
        print(a, a - MAX, b)
        update(a, b)
        print(tree)
    else:
        n = temp[1]
        res = query(7, 8, n)
        print(res)
