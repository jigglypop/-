import sys
sys.stdin = open("7578.txt", "r")
input = sys.stdin.readline
N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
A = [i + 1 for i in range(N)]
B = []
maps = {}
for i in range(N):
    maps[a[i]] = i + 1
for j in b:
    B.append(maps[j])
# [132, 392, 311, 351, 231]
# [392, 351, 132, 311, 231]
# [1, 2, 3, 4, 5]
# [2, 4, 1, 3, 5]

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
