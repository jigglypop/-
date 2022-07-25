import sys
from math import cos, sin, pi
sys.stdin = open('./text/17104.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

def fft(arr, w):
    n = len(arr) // 2
    if n == 0: return
    even = []
    odd = []
    for i in range(n):
        even.append(arr[2 * i])
        odd.append(arr[2 * i + 1])
    ww = w * w
    fft(even, ww)
    fft(odd, ww)
    wk = complex(1, 0)
    for i in range(n):
        arr[i] = even[i] + wk * odd[i]
        arr[i + n] = even[i] - wk * odd[i]
        wk *= w

def multiply(a, b):
    N = max(len(a), len(b))
    n = 1
    while n <= N:
        n *= 2
    n *= 2
    a.extend([0] * (n - N))
    b.extend([0] * (n - N))
    w = complex(cos(2 * pi / n), sin(2 * pi / n))
    fft(a, w)
    fft(b, w)
    c = [a[i] * b[i] for i in range(n)]
    fft(c, 1 / w)
    for i in range(n):
        c[i] = round(c[i].real / n)
    return c

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