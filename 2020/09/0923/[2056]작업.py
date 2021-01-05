import sys
from collections import deque
sys.stdin = open('2056.txt', 'r')
N = int(input())
graph = [[] for _ in range(N+1)]
Q = deque()
dp = [0 for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]
time = [0 for _ in range(N+1)]

for i in range(1, N+1):
    temp = list(map(int, input().split()))
    time[i] = temp[0]
    if temp[1] != 0:
        for j in temp[2:]:
            graph[j].append(i)
        indegree[i] = temp[1]
    else:
        dp[i] = time[i]
        Q.append(i)

while Q:
    work = Q.popleft()
    for i in graph[work]:
        dp[i] = max(dp[i], dp[work] + time[i])
        indegree[i] -= 1
        if indegree[i] == 0:
            Q.append(i)
print(max(dp))
