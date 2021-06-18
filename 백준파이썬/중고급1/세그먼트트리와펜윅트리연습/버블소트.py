import sys
sys.stdin = open("1517.txt", "r")
input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
_nums = sorted(nums)
A = [i + 1 for i in range(N)]
B = []
maps = {}
for i in range(len(nums)):
    maps[nums[i]] = i + 1
for num in _nums:
    B.append(maps[num])
tree = [0] * (N + 1)


def sum(i):
    res = 0
    while i > 0:
        res += tree[i]
        i -= (i & -i)
    return res


def update(i, x):
    while i < len(tree):
        tree[i] += x
        i += (i & -i)


result = 0
for b in B:
    update(b, 1)
    result += sum(N) - sum(b)
print(result)
