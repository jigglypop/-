import sys
from math import *
sys.stdin = open("./text/13575.txt", "r")
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

def fpow(A, N):
    if N == 1:return A
    a = fpow(A, N // 2)
    b = convolution(a, a[::-1])
    return b


N, n = map(int, input().strip().split())
nums = list(map(int, input().strip().split()))
A = [0] * (max(nums) + 1)
for num in nums:
    A[num] = 1
R = A[::]
if n % 2 == 0:
    C = fpow(A, n)
    R = []
else:
    C = fpow(A, n - 1)
C = [0] + [0 if C[i].real == 0 else 1  for i in range(len(C))] 
if len(R) > 0:
    C = convolution(C, R[::-1])
    C = [0] + [0 if C[i].real == 0 else 1  for i in range(len(C))] 
for i in range(len(C)):
    if C[i] == 1:
        print(i, end=" ")
# results = [0] * 100
# for i in range(N - 1, 2 * N - 1):
#     j = i - (M - 1)
#     results[j] += C[i].real
# print(results)