import sys
from math import *
sys.stdin = open('./text/10531.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())

def fft(board, w):
    n = len(board) // 2
    if n == 0:return
    even = board[0::2]
    odd = board[1::2]
    fft(even, w * w)
    fft(odd, w * w)
    cpx = complex(1, 0)
    for i in range(n):
        board[i] = even[i] + cpx * odd[i]
        board[i + n] = even[i] - cpx * odd[i]
        cpx *= w

def multiply(board):
    N = len(board)
    n = 1
    while n <= N:n *= 2
    n *= 2
    board.extend([0] * (n - N))
    w = complex(cos(2 * pi / n), sin(2 * pi / n))
    fft(board, w)
    c = [board[i] ** 2 for i in range(n)]
    fft(c, 1 / w)
    return [round(c[i].real / n) for i in range(n)]

N = 1000000
board = [1] * (N + 1)
board[0] = board[1] = 0
for j in range(4, N + 1, 2):
    board[j] = 0
for i in range(3, N + 1, 2):
    if board[i]:
        for j in range(i * i, N + 1, i):
            board[j] = 0

b = [0] * (N // 2)
for i in range(N // 2):
    b[i] = board[2 * i + 1]

result = multiply(b)
result[1] = 1
for _ in range(int(input())):
    print((result[int(input()) // 2 - 1] + 1) // 2)