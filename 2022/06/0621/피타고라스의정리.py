import sys
sys.stdin = open("./text/5051.txt", "r")
input = sys.stdin.readline

P = 469762049

def FFT(L, inv = False):
    j = 0
    n = len(L)
    for i in range(1, n):
        bit = n >> 1
        while j >= bit:
            j -= bit
            bit >>= 1
        j += bit
        if i < j:
            L[i], L[j] = L[j], L[i]
    Len = 2
    while Len <= n:
        u = pow(3, P // Len, P)
        if inv:
            u = pow(u, P - 2, P)
        for i in range(0, n, Len):
            w = 1
            for k in range(i, i + Len // 2):
                value = L[k + Len // 2] * w
                L[k + Len // 2] = (L[k] - value) % P
                L[k] = (L[k] + value) % P
                w = w * u % P
        Len *= 2
    if inv:
        inv_n = P - (P - 1) // n
        for i in range(n):
            L[i] = L[i] * inv_n % P
    

def multiply(num):
    n = 2
    while n < len(num):n *= 2
    n *= 2
    num += [0 for _ in range(n - len(num))]
    FFT(num)
    value = [i ** 2 % P for i in num]
    FFT(value, inv = True)
    return value
    
result = 0
n = int(input())
A = [0 for _ in range(n)]
for i in range(1, n):
    A[i ** 2 % n] += 1


LL = multiply(A[:])
for i in range(n):
    result += A[i] * LL[i] + A[i] * LL[i + n]
for i in range(n):
    result += A[i] * A[i * 2 % n]
print(result // 2)