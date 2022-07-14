import sys
sys.stdin = open('./text/1605.txt', 'r')
input = sys.stdin.readline
dp = [i for i in range(10000)]
def Int():return int(input().strip())
def Str():return input().strip()

A = Str()
B = Str()
S = A + '$' + B
N = len(S)
SA = [i for i in range(N)]
ISA = [ord(S[i]) for i in range(N)] + [-1]
_ISA = [0] * N + [-1]
t = 1
while t < N:
    SA.sort(key = lambda x : (ISA[x], ISA[min(x + t, N)]))
    for i in range(1, N):
        a, b = SA[i - 1], SA[i]
        if ISA[a] != ISA[b] or ISA[min(a + t, N)] != ISA[min(b + t, N)]:
            _ISA[b] = _ISA[a] + 1
        else:
            _ISA[b] = _ISA[a]
    t *= 2
    ISA = _ISA[:]

LCP = [0] * N
l = 0 
for i in range(N):
    if ISA[i] == 0: continue 
    j = SA[ISA[i] - 1]
    while i + l < N and j + l < N and S[i + l] == S[j + l]:
        l += 1
    LCP[ISA[i]] = l
    if l > 0: 
        l -= 1

print(max(LCP))