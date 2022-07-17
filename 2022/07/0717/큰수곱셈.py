import sys
from decimal import *
sys.stdin = open('./text/22289.txt', 'r')
input = sys.stdin.readline
dp = [i for i in range(10000000)]
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())

p = 469762049
def FFT(L, inv = False):
    j = 0
    n = len(L)
    for i in range(1, n):
        bit = n >> 1
        while j >= bit:
            j -= bit
            bit >>= 1
        j += bit
        if i < j: L[i], L[j] = L[j], L[i]
    m = 2
    while m <= n:
        u = pow(3, p // m, p)
        if inv:
            u = pow(u, p - 2, p)
        for i in range(0, n, m):
            w = 1
            for k in range(i, i + m // 2):
                tmp = L[k + m // 2] * w
                L[k + m // 2] = (L[k] - tmp) % p
                L[k] += tmp
                L[k] %= p
                w *= u
                w %= p
        m *= 2
    if inv:
        invN = p - (p - 1) // n
        for i in range(n):
            L[i] = (L[i] * invN) % p

def multiply(a, b):
    n = 2
    while n < max(len(a), len(b)):
        n *= 2
    n *= 2
    a += [0 for _ in range(n - len(a))]
    b += [0 for _ in range(n - len(b))]
    FFT(a)
    FFT(b)
    result = [(i * j) % p for i, j in zip(a, b)]
    FFT(result, inv = True)
    return result

A, B = input().split()
N = len(A) + len(B) - 1
A = list(map(int, list(A)))
B = list(map(int, list(B)))
if A[0] == 0 or B[0] == 0:
    print(0)
    exit()

C = multiply(A, B)[:N]
result = [0 for _ in range(N + 1)]
for i in reversed(range(1, N + 1)):
    result[i] += C[i - 1] % 10
    result[i - 1] += C[i - 1] // 10
    result[i - 1] += result[i] // 10
    result[i] %= 10

flag = True
for i in result:
    if flag and i == 0:
        continue
    else:
        flag = False
    print(i, end = '')