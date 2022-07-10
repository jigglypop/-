import sys
sys.stdin = open('./text/2042.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())

N, M, K = Split()
board = [0] * N + [Int() for _ in range(N)]
for i in reversed(range(1, N)):
    board[i] = board[2 * i] + board[2 * i ^ 1]
    a, b, c = Split()
    b += N - 1
    if a == 1:
        i = b
        x = c
        board[i] = x
        while i > 1:
            board[i // 2] = board[i] + board[i ^ 1]
            i //= 2
    else:
        c += N - 1
        l = b
        r = c
        result = 0
        while l <= r:
            if l % 2:
                result += board[l]
                l += 1
            if not (r % 2):
                result += board[r]
                r -= 1
            l >>= 1
            r >>= 1
        print(result)