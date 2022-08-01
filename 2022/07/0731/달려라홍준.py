import sys
sys.stdin = open('./text/1298.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

N, M = Split()
board = [0] * N + List()
for i in reversed(range(1, N)):
    board[i] = max(board[i * 2], board[i * 2 ^ 1])

def query(l, r):
    l += N - 1
    r += N - 1
    result = 0
    while l <= r:
        if l % 2:
            result = max(result, board[l])
            l += 1
        if not r % 2:
            result = max(result, board[r])
            r -= 1
        l >>= 1
        r >>= 1
    return result

for i in range(M, N - M + 2):
    print(query(i - M + 1, i + M - 1), end=" ")
