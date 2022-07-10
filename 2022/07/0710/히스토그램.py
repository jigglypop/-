import sys
input = sys.stdin.readline
N = int(input())
graph = [int(input()) for _ in range(N)] + [0]
result = 0
cursor = 0
a = 0
S = [(0,graph[0])]
for i in range(1, N + 1):
    cursor = i
    while S and S[-1][1]>graph[i]:
        cursor,temp=S.pop()
        result = max(result,temp*(i-cursor))
    S.append((cursor,graph[i]))
print(result)