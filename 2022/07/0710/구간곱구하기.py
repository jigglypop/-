import sys
sys.stdin = open('./text/11505.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())
P = 1000000007
N, m, k = Split()
board = [1] * N + [Int() for _ in range(N)]
for i in reversed(range(1, N)):
    board[i] = (board[2 * i] * board[2 * i ^ 1]) % P

for _ in range(m + k):
    a, b, c = Split()
    b += N - 1
    if a == 1:
        i = b
        x = c
        board[i] = x
        while i > 1:
            board[i // 2] = (board[i] * board[i ^ 1]) % P
            i //= 2
    else:
        c += N - 1
        l = b
        r = c
        res = 1
        while l <= r:
            if l % 2 == 1:
                res = (res * board[l]) % P
                l += 1
            if r % 2 == 0:
                res = (res * board[r]) % P
                r -= 1
            l >>= 1
            r >>= 1
        print(res)
