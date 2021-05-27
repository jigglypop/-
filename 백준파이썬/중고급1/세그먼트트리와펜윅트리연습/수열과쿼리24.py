import sys
sys.stdin = open("17408.txt", "r")
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
tree = [0] * N + [i for i in range(N)]
for i in reversed(range(1, N)):
    if A[tree[2 * i]] > A[tree[2 * i ^ 1]]:
        tree[i] = tree[2 * i]
    else:
        tree[i] = tree[2 * i ^ 1]


def update(i, x):
    A[i - N] = x
    while i > 1:
        if A[tree[i]] > A[tree[i ^ 1]]:
            tree[i // 2] = tree[i]
        else:
            tree[i // 2] = tree[i ^ 1]
        i //= 2


def query(l, r):
    res = 0
    idx = -1
    while l < r:
        if l % 2:
            if res < A[tree[l]]:
                idx = tree[l]
                res = A[tree[l]]
            l += 1
        if not (r % 2):
            if res < A[tree[r]]:
                idx = tree[r]
                res = A[tree[r]]
            r -= 1
        l >>= 1
        r >>= 1
    if l == r:
        if res < A[tree[r]]:
            idx = tree[r]
            res = A[tree[r]]
    return res, idx


M = int(input())
for _ in range(M):
    a, b, c = map(int, input().split())
    b += N - 1
    if a == 1:
        update(b, c)
    else:
        c += N - 1
        v, p = query(b, c)
        p += N
        a1, _ = query(b, p-1)
        a2, _ = query(p+1, c)
        temp = [a1, a2, A[p-N]]
        temp.sort()
        print(temp[1] + temp[2])
