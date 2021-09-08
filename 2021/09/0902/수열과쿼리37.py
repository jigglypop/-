import sys
sys.stdin = open('18436.txt', 'r')
input = sys.stdin.readline
N = int(input())
nums = [0] + list(map(int, input().split()))
treeA = [0] * (N+1)
treeB = [0] * (N+1)


def update(i, a, b):
    while i < N + 1:
        treeA[i] += a
        treeB[i] += b
        i += (i & -i)


def sum(flag, i):
    tree = []
    if flag == 2:
        tree = treeA
    else:
        tree = treeB
    s = 0
    while i > 0:
        s += tree[i]
        i -= (i & -i)
    return s


for i in range(1, len(nums)):
    update(i, nums[i] % 2, 1 - nums[i] % 2)

for _ in range(int(input())):
    q, a, b = map(int, input().split())
    if q == 1:
        _x = nums[a]
        x = b
        if _x % 2 == 1 and x % 2 == 0:
            update(a, 1, -1)
        elif _x % 2 == 0 and x % 2 == 1:
            update(a, -1, 1)
        nums[a] = b
    else:
        print(sum(q, b) - sum(q, a-1))
