import sys
from math import cos, sin, pi
sys.stdin = open("./text/1037.txt", "r")
input = sys.stdin.readline

def fft(A, W):
    N = len(A)
    if N == 1: return A
    E = fft(A[::2], W * W)
    O = fft(A[1::2], W * W)
    return [E[i] + (W ** i) * O[i] for i in range(N//2)] + [E[i] - (W ** i) * O[i] for i in range(N//2)]

def multiply(A, B):
    n = 1
    while n < len(A): n *= 2
    n *= 2
    M = n - len(A)
    W = cos(2 * pi / n) + 1j * sin(2 * pi / n)
    A_fft, B_fft = fft(A + [0] * M, W), fft(B + [0] * M , W)
    C = fft([A_fft[i] * B_fft[i] for i in range(n)], W.conjugate())
    return [round((C[i]/n).real) for i in range(n)]

N = int(input())
A = list(map(int,input().split()))[::-1]
B = list(map(int,input().split()))
A += [0] * len(A)
B += B[:]
C = multiply(A, B)
print(C)
print(max(C))
