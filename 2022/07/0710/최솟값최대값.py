import sys
sys.stdin = open('./text/2357.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())
INF = sys.maxsize
N, M = Split()
maxBoard = [INF] * N + [Int() for _ in range(N)]
minBoard = maxBoard[::]
for i in reversed(range(1, N)):
    maxBoard[i] = max(maxBoard[2 * i], maxBoard[2 * i ^ 1])
    minBoard[i] = min(minBoard[2 * i], minBoard[2 * i ^ 1])

for _ in range(M):
    l, r = Split()
    l += N - 1
    r += N - 1
    Max = -INF
    Min = INF
    while l <= r:
        if l % 2 == 1:
            Min = min(Min, minBoard[l])
            Max = max(Max, maxBoard[l])
            l += 1
        if r % 2 == 0:
            Min = min(Min, minBoard[r])
            Max = max(Max, maxBoard[r])
            r -= 1
        l >>= 1
        r >>= 1
    print(f"{Min} {Max}")  