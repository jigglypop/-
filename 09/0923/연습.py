from collections import deque
import sys
import heapq
sys.stdin = open('1948.txt', 'r')


n = int(input())
m = int(input())
degree = [0] * (n+1)
check = [0] * (n+1)
result = [0] * (n+1)
G_inv = [[] for _ in range(n+1)]
G_rev = [[] for _ in range(n+1)]

for i in range(m):
    s, e, t = map(int, input().split())
    G_inv[s].append((e, t))
    G_rev[e].append((s, t))
    degree[e] += 1

start, end = map(int, input().split())
Q = deque()
Q.append(start)
while Q:
    ss = Q.popleft()
    for next, time in G_inv[ss]:
        if result[next] <= time + result[ss]:
            result[next] = time + result[ss]
        degree[next] -= 1
        if degree[next] == 0:
            Q.append(next)
count = 0
Q.append(end)
while Q:
    ee = Q.popleft()
    for pre, time in G_rev[ee]:
        if result[ee] - result[pre] == time:
            count += 1
            if check[pre] == 0:
                Q.append(pre)
                check[pre] = 1
print(result[end])
print(count)
