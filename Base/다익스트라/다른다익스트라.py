from heapq import heappop, heappush
import sys
sys.stdin = open("다익스트라.txt", "r")

input = sys.stdin.readline
INF = sys.maxsize
V, E = map(int, input().split())
start = int(input())
graph = [[] for i in range(V+1)]
distance = [INF]*(V+1)
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])

heap = []  # 우선순위 큐 -> 힙으로 구현해줌
distance = [INF for _ in range(V+1)]  # 답이 될 start로부터의 거리
distance[start] = 0  # 자기 자신은 0
heappush(heap, (0, start))  # 자기 자신으로부터 우선순위 큐를 시작한다

while heap:
    mid = heappop(heap)  # 현재 가장 가까운 거리의 노드를 pop [거리, 노드 위치]
    for end in graph[mid[1]]:  # 가장 가까운 노드에 연결된 모든 노드들 end에 대하여
        if distance[end[0]] > mid[0] + end[1]:  # mid노드를 거치는 게 end로 바로 가는 것보다 효율적이라면
            distance[end[0]] = mid[0] + end[1]  # 해당 거리를 저장
            # 큐에 [갱신된 거리, 노드 위치] 삽입
            heappush(heap, (distance[end[0]], end[0]))

# 출력
for i in range(1, V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
