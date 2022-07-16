
import sys
sys.setrecursionlimit(10 ** 5)
sys.stdin = open('./text/6549.txt', 'r')
input = sys.stdin.readline
dp = [i for i in range(10000)]
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

N = Int()
board = [Int() for _ in range(N)]
INF = sys.maxsize
board = [(0, 0)] * N + board
for i in reversed(range(N)):
    if board[2 * i][1] > board[2 * i ^ 1][1]:
        board[i] = board[2 * i ^ 1]
    else:
        board[i] = board[2 * i]

def query(l, r):
    res = (0, INF)
    while l <= r:
        if l % 2:
            if res[1] > board[l][1]:
                res = board[l]
            l += 1
        if not (r % 2):
            if res[1] > board[r][1]:
                res = board[r]        
            r -= 1
        l >>= 1
        r >>= 1
    return res

def divide(s, e):
    i, Min = query(s, e)
    i += N
    A = (e - s + 1) * Min
    if s <= i - 1:
        A = max(A, divide(s, i - 1))
    if e >= i + 1:
        A = max(A, divide(i + 1, e))
    return A

print(divide(1 + N - 1, N + N - 1))
