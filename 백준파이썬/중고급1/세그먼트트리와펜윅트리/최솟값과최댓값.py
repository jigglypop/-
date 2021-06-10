import sys
sys.stdin = open("2357.txt", "r")
N, M = map(int, input().split())

temp = [int(input()) for _ in range(N)]
treeMax = [0] * N + temp
treeMin = [0] * N + temp
for i in reversed(range(N)):
    treeMin[i] = min(treeMin[2 * i], treeMin[2 * i ^ 1])
    treeMax[i] = max(treeMax[2 * i], treeMax[2 * i ^ 1])


def min_query(l, r):
    result = sys.maxsize
    while l <= r:
        if l % 2:
            result = min(result, treeMin[l])
            l += 1
        if not (r % 2):
            result = min(result, treeMin[r])
            r -= 1
        l >>= 1
        r >>= 1
    return result


def max_query(l, r):
    Min = sys.maxsize
    Max = 0
    while l <= r:
        if l % 2:
            Max = max(Max, treeMax[l])
            Min = min(Min, treeMin[l])
            l += 1
        if not (r % 2):
            Max = max(Max, treeMax[r])
            Min = min(Min, treeMin[l])
            r -= 1
        l >>= 1
        r >>= 1
    return Min, Max


for _ in range(M):
    a, b = map(int, input().split())
    a += N - 1
    b += N - 1
    print(min_query(a, b), max_query(a, b))
