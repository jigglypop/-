import sys
sys.stdin = open("./text/9249.txt", "r")
input = sys.stdin.readline
A = input()
B = input()
C = A + '1' + B
N = len(C)
SA = [i for i in range(N)]
g = [ord(C[i]) for i in range(N)] + [-1]
t = 1
while t < N:
    ng = [0] * N + [-1] 
    SA.sort(key = lambda x :(g[x], g[min(x + t, N)]))
    for i in range(1, N):
        a, b = SA[i-1], SA[i]
        if g[a] != g[b] or g[min(a + t, N)] != g[min(b + t, N)]:
            ng[b] = ng[a] + 1
        else:
            ng[b] = ng[a]
    t *= 2
    g = ng[:]
LCP = [0] * N
l = 0 
for i in range(N):
    if not g[i]: continue 
    j = SA[g[i] - 1]
    while i + l < N and j + l < N and C[i + l] == C[j + l]:
        l += 1
    LCP[g[i]] = l
    if l: l -= 1
result = (0, 0) 
for i, j in enumerate(LCP):
    if 0 <= SA[i - 1] + j - 1 < len(A) and len(A) < SA[i] + j - 1 <len(C):
        result = max(result, (j, i))
    if 0 <= SA[i] + j - 1 < len(A) and len(A) < SA[i - 1] + j - 1 <len(C):
        result = max(result, (j, i))
    
l, start = result
print(l)
print(C[SA[start] : SA[start] + l])