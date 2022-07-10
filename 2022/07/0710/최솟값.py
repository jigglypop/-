import sys
sys.stdin = open('./text/10868.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())
INF = sys.maxsize
N, M = Split()
board = [INF] * N + [Int() for _ in range(N)]
for i in reversed(range(1, N)):
    board[i] = min(board[2 * i], board[2 * i ^ 1])

for _ in range(M):
    l, r = Split()
    l += N - 1
    r += N - 1
    result = INF
    while l <= r:
        if l % 2 == 1:
            result = min(result, board[l])
            l += 1
        if r % 2 == 0:
            result = min(result, board[r])
            r -= 1
        l >>= 1
        r >>= 1
    print(result)  