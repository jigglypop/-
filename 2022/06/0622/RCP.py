import sys
from math import *
sys.stdin = open("./text/14958.txt", "r")
input = sys.stdin.readline

def FFT(a, w):
    n = len(a)
    if n == 1: return
    even = a[0::2]
    odd = a[1::2]
    FFT(even, w * w)
    FFT(odd, w * w)
    wp = complex(1, 0)
    for i in range(n//2):
        a[i] = even[i] + wp * odd[i]
        a[i + n//2] = even[i] - wp * odd[i]
        wp *= w
    return a

def convolution(a, b):
    n = 1
    while (n < len(a)) or (n < len(b)): n *= 2
    n *= 2
    a.extend([0] * (n - len(a)))
    b.extend([0] * (n - len(b)))
    c = [0 for _ in range(n)]
    w = complex(cos(2 * pi/n), sin(2 * pi/n)) 
    inv = w.conjugate()
    a = FFT(a, w)
    b = FFT(b, w)
    for i in range(n):
        c[i] = a[i]*b[i]
    c = FFT(c, inv)
    for i in range(n):
        c[i] /= complex(n, 0)
        c[i] = complex(round(c[i].real), round(c[i].imag))
    return c

N, M = map(int, input().split())
A = list(map(str, input()))
B = list(map(str, input()))
B.reverse()
results = [0] * N
RPS = ['R', 'P', 'S']
for j in range(3):
    X = [1 if i == RPS[j % 3] else 0 for i in A]
    Y = [1 if i == RPS[(j + 1) % 3] else 0 for i in B]
    Z = convolution(X, Y)
    for i in range(M - 1, N + M - 1):
        j = i - (M - 1)
        results[j] += Z[i].real
MAX = 0
for i in range(N):
    MAX = max(MAX, results[i])
print(int(MAX))
