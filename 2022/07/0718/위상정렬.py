import sys
from collections import deque
sys.stdin = open('./text/2252.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()
N, M = Split()
graph = [[] for _ in range(N + 1)]
check = [0] * (N + 1)

for i in range(M):
    A, B = Split()
    graph[A].append(B)
    check[B] += 1
Q = deque(list(filter(lambda x: check[x] == 0, [i + 1 for i in range(N)])))
while Q:
    u = Q.popleft()
    for v in graph[u]:
        check[v] -= 1
        if check[v] == 0:
            Q.append(v)
    print(u, end=" ")