import sys
from unittest import result
sys.stdin = open('./text/10413.txt', 'r')
input = sys.stdin.readline
dp = [i for i in range(10000)]
def Int():return int(input().strip())
def Str():return input().strip()

def SA_ISA(S):
    N = len(S)
    SA = [i for i in range(N)] 
    ISA = [ord(S[i]) for i in range(N)] + [-1]
    _ISA = [0] * N + [-1]
    t = 1
    while t < N:
        SA.sort(key = lambda x: (ISA[x], ISA[min(x + t, N)]))
        for i in range(1, N):
            a, b = SA[i], SA[i - 1]
            if ISA[a] != ISA[b] or ISA[min(a + t, N)] != ISA[min(b + t, N)]:
                _ISA[a] = _ISA[b] + 1
            else:
                _ISA[a] = _ISA[b]
        t *= 2
        ISA = _ISA[:]

    return SA, ISA

def LCP(S):
    N = len(S)
    SA, ISA = SA_ISA(S)
    l = 0
    lcp = [0] * N
    for i in range(N):
        if ISA[i] == 0:continue
        j = SA[ISA[i] - 1]
        while i + l < N and j + l < N and S[i + l] == S[j + l]:
            l += 1
        lcp[ISA[i]] = l
        if l > 0:
            l -= 1
    return lcp

for _ in range(Int()):
    S = Str()
    N = len(S)
    lcp = LCP(S)
    results = 0
    for i in range(1, N):
        if lcp[i] > lcp[i - 1]:
            results += lcp[i] - lcp[i - 1]
    print(results)
    