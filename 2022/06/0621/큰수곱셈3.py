import sys
from math import *
sys.stdin = open("./text/15576.txt", "r")
input = sys.stdin.readline

def FFT(f, w):
    n = len(f)
    if n == 1: return
    even = f[0::2]
    odd = f[1::2]
    FFT(even, w*w)
    FFT(odd, w*w)
    w_k = complex(1, 0)
    for i in range(n//2):
        f[i] = even[i] + w_k * odd[i]
        f[i + n//2] = even[i] - w_k * odd[i]
        w_k *= w

def convolution(a, b):
    n = 1
    while (n < len(a)) or (n < len(b)): n *= 2
    n *= 2
    a.extend([0]*(n-len(a)))
    b.extend([0]*(n-len(b)))
    c = [0 for _ in range(n)]
    w = complex(cos(2*pi/n), sin(2*pi/n)) 
    inv_w = w.conjugate()
    FFT(a, w)
    FFT(b, w)
    for i in range(n):
        c[i] = a[i]*b[i]
    FFT(c, inv_w)
    for i in range(n):
        c[i] /= complex(n, 0)
        c[i] = complex(c[i].real, c[i].imag)
    return c

def decimal(a):
    return list(map(float, (str(a) + '0')[::-1]))

a, b = map(int, input().split())
A = decimal(a)
B = decimal(b)
C = convolution(A, B)
C = [C[i].real for i in range(len(C))][1:]
result = 0
for i in range(1, len(C)):
    result += C[i] * 10 ** (i - 1)
print(result)
