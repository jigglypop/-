import sys
sys.stdin = open("./text/3033.txt", "r")
input = sys.stdin.readline
N = int(input())
C = input()
SA = [i for i in range(N + 1)]
_g = [0] * (N + 1) 
g = [ord(C[i]) for i in range(N)] + [-1]
_g[SA[0]] = 0
_g[N] = -1
t = 1
while t < N:
    SA.sort(key = lambda x :(g[x], g[min(x + t, N)]))
    for i in range(1, N):
        a, b = SA[i-1], SA[i]
        if g[a] != g[b] or g[min(a + t, N)] != g[min(b + t, N)]:
            _g[b] = _g[a] + 1
        else:
            _g[b] = _g[a]
    t *= 2
    g = _g[:]

LCP = [0] * N
l = 0 
for i in range(N):
    if not g[i] or g[i] - 1 > N: continue 
    j = SA[g[i] - 1]
    while i + l < N and j + l < N and C[i + l] == C[j + l]:
        l += 1
    LCP[g[i]] = l
    if l: l -= 1
print(max(LCP))
