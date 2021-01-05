import sys
from collections import deque
from heapq import heappop, heappush
sys.stdin = open('1516.txt', 'r')
input = sys.stdin.readline


N = int(input())
time = [0] * (N+1)
next_building = dict()
indegree = [0] * (N+1)
for i in range(1, N+1):
    temp = list(map(int, input().split()))
    time[i] = temp[0]
    for temp2 in temp[1:-1]:
        ne = next_building.get(temp2, [])
        ne.append(i)
        next_building[temp2] = ne
        indegree[i] += 1
result = [0] * (N+1)

Q = deque()
for i in range(1, N+1):
    result[i] = time[i]
    if indegree[i] == 0:
        Q.append(i)
print(result)
print(time)
while Q:
    q = Q.popleft()
    if q in next_building:
        for nb in next_building[q]:
            result[nb] = max(result[nb], result[q] + time[nb])
            indegree[nb] -= 1
            if indegree[nb] == 0:
                Q.append(nb)

for i in range(1, N+1):
    print(result[i])
