import sys
sys.stdin = open("./text/13264.txt", "r")
input = sys.stdin.readline
word = input().strip()
N = len(word)
SA = [i for i in range(N)]
G = [ord(word[i]) for i in range(N)] + [-1]
t = 1
while t < N:
    nG = [0] * N + [-1]
    SA.sort(key = lambda x: (G[x], G[min(x + t, N)]))
    for i in range(1, N):
        a, b = SA[i], SA[i - 1]
        if G[a] != G[b] or  G[min(a + t, N)] != G[min(b + t, N)]:
            nG[a] = nG[b] + 1
        else:
            nG[a] = nG[b]
    t *= 2
    G = nG[:]
for sa in SA:
    print(sa)
