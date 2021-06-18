import sys
sys.stdin = open("3006.txt", "r")
input = sys.stdin.readline
N = int(input())
B = [int(input()) for _ in range(N)]
tree = [0] * (N+1)


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


maps = {}
for i in range(1, N+1):
    update(i, 1)
    maps[B[i-1]] = i

left = 1
right = N
for i in range(1, N+1):
    if i % 2 == 1:
        a = maps[left]
        update(a, -1)
        print(sum(a))
        left += 1
    else:
        a = maps[right]
        update(a, -1)
        print(sum(N) - sum(a))
        right -= 1
