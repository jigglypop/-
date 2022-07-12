import sys
sys.stdin = open("./text/11657.txt", "r")
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())
INF = sys.maxsize
Y, X = Split()
board = [list(Split()) for _ in range(X)]
def bellman_ford():
    dist = [INF] * (Y + 1)
    dist[1] = 0
    for y in range(Y):
        for x in range(X):
            u, v, cost = board[x]
            if dist[u] != INF and dist[v] > dist[u] + cost:
                dist[v] = dist[u] + cost
                if y == Y - 1: return [-1]
    if Y != 1 :return [dist[0]]
    else: return [-1 if x == INF else x for x in dist[2:]]
for result in bellman_ford():
    print(result)