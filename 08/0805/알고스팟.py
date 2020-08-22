import sys
import heapq
sys.stdin = open("알고스팟3.txt", 'r')
M, N = map(int, input().split())
m = [list(input().rstrip()) for _ in range(N)]
crush = [[-1] * M for _ in range(N)]


def dijkstra():
    q = []
    heapq.heappush(q, (0, (0, 0)))
    crush[0][0] = 0
    di = ((-1, 0), (1, 0), (0, 1), (0, -1))
    while q:
        cnt, (hy, hx) = heapq.heappop(q)
        if hy == N-1 and hx == M-1:
            break
        for dy, dx in di:
            ny, nx = hy + dy, hx + dx
            if 0 <= ny < N and 0 <= nx < M:
                if crush[ny][nx] < 0:
                    crush[ny][nx] = cnt
                    if m[ny][nx] == '1':
                        heapq.heappush(q, (cnt+1, (ny, nx)))
                    else:
                        heapq.heappush(q, (cnt, (ny, nx)))


dijkstra()
print(crush[N-1][M-1])
