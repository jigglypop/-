import sys
sys.stdin = open('./text/9240.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(float, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

C = lambda x: complex(x[0], x[1])
CP = lambda a, b, c, d: ((b - a).conjugate() * (d - c)).imag
N = Int()
A = set(C(List()) for _ in range(N))
A = sorted(A, key = lambda c: (c.real,c.imag))
if len(A) == 1:
    print(0)
else:
    U = [] 
    L = []
    for p in A:
        while len(U) > 1 and CP(U[-2], U[-1], U[-1], p) >= 0: 
            U.pop()
        while len(L) > 1 and CP(L[-2], L[-1], L[-1], p) <= 0: 
            L.pop()
        U.append(p)
        L.append(p)
    N = len(U) + len(L) - 2
    A = U[:] + L[-2:0:-1]
    A += A
    a = 0
    b = 1
    result = 0
    while a < N:
        result = max(result, abs(A[b] - A[a]))
        if CP(A[a], A[a + 1], A[b], A[b + 1]) < 0:
            b += 1
        else: 
            a += 1
    print("%.8f"%result)