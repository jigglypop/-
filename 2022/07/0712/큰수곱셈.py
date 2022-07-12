import sys
from math import *
sys.stdin = open('./text/15576.txt', 'r')
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

a, b = Split()
_A = list(map(int, list(str(a)[::-1])))
_B = list(map(int, list(str(b)[::-1])))
C = list(filter(lambda x: x != 0, multiply(_A, _B)))
result = 0
for i in range(len(C)):
    c = C[i]
    result += c * 10 ** i
print(result)
