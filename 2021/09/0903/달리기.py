import sys
sys.setrecursionlimit(10**6)
sys.stdin = open("2517.txt", "r")
input = sys.stdin.readline
N = int(input())
nums = [int(input()) for _ in range(N)]
tree = [0] * (N + 1)
nums_sort = sorted(nums)
nums_obj = {}
for i in range(len(nums_sort)):
    num = nums_sort[i]
    nums_obj[num] = i + 1


def update(i, x):
    while i < len(tree):
        tree[i] += 1
        i += (i & -i)


def sum(i):
    s = 0
    while i > 0:
        s += tree[i]
        i -= (i & -i)
    return s


i = 2
for num in nums:
    idx = nums_obj[num]
    update(idx, 1)
    print(i - sum(idx))
    i += 1
