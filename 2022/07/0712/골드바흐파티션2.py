import sys
from math import *
sys.stdin = open('./text/17104.txt', 'r')
input = sys.stdin.readline
dp = [i for i in range(10000000)]
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())
def L(n, arr):
    if len(arr) == 1:return [n for _ in range(arr[0])]
    return [L(n, arr[1:]) for _ in range(arr[0])]

def fft(board, w):
    n = len(board) // 2
    if n == 0:return
    even = board[0::2]
    odd = board[1::2]
    fft(even, w * w)
    fft(odd, w * w)
    wp = complex(1, 0)
    for i in range(n):
        board[i] = even[i] + wp * odd[i]
        board[i + n] = even[i] - wp * odd[i]
        wp *= w

def multiply(A, B):
    N = max(len(A), len(B))
    n = 1
    while n <= N:
        n *= 2
    n *= 2
    A.extend([0] * (n - N))
    B.extend([0] * (n - N))
    w = complex(cos(2 * pi / n), sin(2 * pi / n))
    fft(A, w)
    fft(B, w)
    c = [A[i] * B[i] for i in range(n)]
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
B = [board[2 * i + 1] for i in range(N // 2)]
result = multiply(B[:], B[:])
result[1] = 1
for _ in range(Int()):
    print((result[Int() // 2 - 1] + 1) // 2)