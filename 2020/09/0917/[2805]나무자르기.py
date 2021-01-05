import sys
sys.stdin = open('2805.txt', 'r')

N, M = map(int, input().split())
trees = list(map(int, input().split()))
start, end = 1, max(trees)
while start <= end:
    mid = (start + end) // 2
    rest = 0
    for tree in trees:
        if tree >= mid:
            rest += tree - mid
    if rest >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)
