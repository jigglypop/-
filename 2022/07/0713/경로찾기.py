import sys
sys.stdin = open('./text/11403.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())
def L(n, arr):
    if len(arr) == 1:return [n for _ in range(arr[0])]
    return [L(n, arr[1:]) for _ in range(arr[0])]

N, M = Split()
board = [0] + list(Split())
for i in range(1, len(board)):
    board[i] += board[i - 1]

Max = -sys.maxsize
for j in range(M, len(board)):
    Max = max(Max, board[j] - board[j - M])
print(Max)