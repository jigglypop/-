import sys
sys.stdin = open('2110.txt', 'r')

N, C = map(int, input().split())
routers = [int(input()) for _ in range(N)]

routers.sort()
start, end = routers[1] - routers[0], routers[-1] - routers[0]
_max = 0
while start <= end:
    mid = (start + end) // 2
    idx, result = 0, 1
    for i in range(1, len(routers)):
        if routers[idx] + mid <= routers[i]:
            result += 1
            idx = i
    if result < C:
        end = mid - 1
    else:
        _max = mid
        start = mid + 1
print(_max)
