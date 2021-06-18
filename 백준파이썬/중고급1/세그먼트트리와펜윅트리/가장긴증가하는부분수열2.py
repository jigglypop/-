import sys
sys.stdin = open("12015.txt", "r")
MAX = 1000001
N = int(input())
nums = list(map(int, input().split()))
tree = [0] * 2 * MAX


def update(i, x):
    tree[i] = x
    while i > 1:
        tree[i // 2] = max(tree[i], tree[i ^ 1])
        i //= 2


def query(l, r):
    res = 0
    while l <= r:
        if l % 2:
            res = max(res, tree[l])
            l += 1
        if not (r % 2):
            res = max(res, tree[r])
            r -= 1
        l >>= 1
        r >>= 1
    return res


Max = 0
for num in nums:
    res = query(MAX + 1, MAX + num - 1) + 1
    Max = max(res, Max)
    update(MAX + num, res)
print(Max)
