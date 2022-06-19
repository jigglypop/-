import sys
from cmath import exp, pi
sys.stdin = open("./text/1037.txt", "r")
input = sys.stdin.readline

def fft(a, flag = 1):
    N=len(a)
    if N==1: return a
    E = fft(a[0::2], flag)
    O = fft(a[1::2], flag)
    wp = [exp(flag * 2j * pi * i/N) for i in range(N//2)]
    return [E[i] + wp[i] * O[i] for i in range(N//2)] + [E[i] - wp[i] * O[i] for i in range(N//2)]

def ifft(a):
    return fft(a, -1)
 
M = int(input())
N = 2 * M

A = list(map(int, input().split()))
B = list(map(int, input().split()))[::-1]

for i in range(18):
    if M == 2 ** i:
        A += A[:]
        B += [0] * M
        break
    elif N < 2 ** i:
        _N = 2 ** i
        N, _N = _N, N
        A += [0] * (N - _N//2)
        B += [0] * (N - _N) + B[:]
        break

A_fft = fft(A)
B_fft = fft(B)
print(A_fft)
print(B_fft)
C = [A_fft[i] * B_fft[i] for i in range(N)]
C_ifft = list(map(lambda x: round(x.real/N), ifft(C)))
print(max(C_ifft))