from collections import deque
import sys
sys.stdin = open("12851.txt", "r")
MAX = 200000
check = [False]*MAX
dist = [0]*MAX
count = [0]*MAX
n, m = map(int, input().split())
check[n] = True
dist[n] = 0
count[n] = 1
Q = deque()
Q.append(n)
while Q:
    now = Q.popleft()
    for _next in [now-1, now+1, now*2]:
        if 0 <= _next < MAX:
            if not check[_next]:
                Q.append(_next)
                check[_next] = True
                dist[_next] = dist[now]+1
                count[_next] = count[now]
            elif dist[_next] == dist[now]+1:
                count[_next] += count[now]
print(dist[m])
print(count[m])
