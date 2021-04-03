from collections import deque, defaultdict
import sys
sys.stdin = open('2316.txt', 'r')


def Dinic(G, C, s, t):
    def send(u, limit):
        if limit <= 0:
            return 0
        if u == t:
            return limit
        val = 0
        for v in G[u]:
            res = C[(u, v)]-flow[(u, v)]
            if level[v] == level[u]+1 and res > 0:
                a = send(v, min(limit-val, res))
                flow[(u, v)] += a
                flow[(v, u)] -= a
                val += a
        if val == 0:
            level[u] -= 1
        return val
    Q, tot, n, flow = deque(), 0, len(G), defaultdict(int)
    while 1:
        Q.append(s)
        level = [-1]*n
        level[s] = 0
        while len(Q) > 0:
            u = Q.popleft()
            for v in G[u]:
                if level[v] == -1 and C[(u, v)] > flow[(u, v)]:
                    level[v] = level[u]+1
                    Q.append(v)
        if level[t] == -1:
            return tot  # , flow
        tot += send(s, sum(C[(s, v)] for v in G[s]))


def addedge(i, j, cap):
    G[i].append(j)
    G[j].append(i)
    C[(i, j)] += cap


input = sys.stdin.readline
n, p = map(int, input().split())
G = [[] for i in range(2*n)]
C = defaultdict(int)

for i in range(n):
    addedge(i, i+n, 1)
for i in range(p):
    a, b = sorted(map(int, input().split()))
    addedge(a+n-1, b-1, 1)
    addedge(b+n-1, a-1, 1)
print(Dinic(G, C, n, 1))
