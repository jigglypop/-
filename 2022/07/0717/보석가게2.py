
from math import cos, pi, sin
import sys
sys.stdin = open('./text/13575.txt', 'r')
input = sys.stdin.readline
dp = [i for i in range(10000)]
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

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

def fft_pow(a, b):
    if b == 1:
        return a
    else:
        m = fft_pow(a, b // 2)
        if b % 2 == 0:
            return multiply(m[:], m[:])
        else:
            return multiply(multiply(m[:], m[:])[:] , a[:])

M, K = Split()
A = [0] * 1001
nums = List()
for num in nums:
    A[num] = 1
result = fft_pow(A, K)
for i in range(len(result)):
    if result[i] > 0:
        print(i, end=" ")