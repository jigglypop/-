import sys
sys.stdin = open('11375.txt')

N, M = map(int, input().split())
print(N, M)

C = [[0] * (N+1) for _ in range(N+1)]
path = [[] for _ in range(N+1)]
for i in range(N):
    a = i+1
    temp = list(map(int, input().split()))
    for b in temp[1:]:
        path[a].append(b)
        path[b].append(a)
        C[a][b] += 1
        C[b][a] += 1

print(C)
