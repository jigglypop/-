input = sys.stdin.readline
n, m, k = Split()
board = [0] * n + [int(input()) for _ in range(n)]
for i in reversed(range(1, n)):
    board[i] = board[2 * i] + board[2 * i ^ 1]
for _ in range(m + k):
    a, b, c = Split()
    b += n - 1
    if a == 1:
        i = b
        x = c
        board[i] = x
        while i > 1:
            board[i // 2] = board[i] + board[i ^ 1]
            i //= 2
    else:
        c += n - 1
        l = b
        r = c
        res = 0
        while l <= r:
            if l % 2:
                res += board[l]
                l += 1
            if not (r % 2):
                res += board[r]
                r -= 1
            l >>= 1
            r >>= 1
        print(res)

