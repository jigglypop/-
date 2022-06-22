import sys
from math import *
sys.stdin = open("./text/20176.txt", "r")
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

a = int(input())
A = list(map(int, input().strip().split()))
b = int(input())
B = list(map(int, input().strip().split()))
c = int(input())
C = list(map(int, input().strip().split()))
Min = sys.maxsize
Max = -sys.maxsize
for d in A + B + C:
    Min = min(Min, d)
    Max = max(Max, d)

Min = Min * -1 if Min <= 0 else 0
D = [0 for i in range(3* (Max + Min + 1))]
E = [0 for i in range(3* (Max + Min + 1))]
F = [0 for i in range(3* (Max + Min + 1))]

for i in range(len(A)):
    a = A[i] + Min + 1
    D[a] = 1

for i in range(len(B)):
    a = B[i] + Min + 1
    E[2* a] = 1

for i in range(len(C)):
    a = C[i] + Min + 1
    F[a] = 1

result = 0
G = convolution(D, F)
G = [G[i].real if G[i].real != 0 else 0 for i in range(len(G))]
for i in range(len(E)):
    if E[i] == 1 and G[i] != 0:
        result += G[i]
print(result)