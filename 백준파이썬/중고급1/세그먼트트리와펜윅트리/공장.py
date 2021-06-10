import sys
sys.stdin = open("7578.txt", "r")
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
tree = [0] * (2 * N)
nums = {}
for i in range(len(B)):
    b = B[i]
    nums[b] = i


def update(i, x):
    tree[i] = x
    while i > 1:
        tree[i // 2] = tree[i] + tree[i ^ 1]
        i //= 2


def query(l, r):
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
    return res


result = 0
for a in A:
    idx = nums[a]
    update(N + idx, 1)
    result += query(N + idx + 1, 2 * N - 1)
print(result)
