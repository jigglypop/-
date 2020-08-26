from pprint import pprint
import sys
sys.stdin = open('2563.txt', 'r')

N = int(input())
visited = [[0] * 101 for _ in range(101)]
for _ in range(N):
    X, Y = map(int, input().split())
    for y in range(Y, Y+10):
        for x in range(X, X+10):
            visited[y][x] = 1
result = 0
for y in range(101):
    for x in range(101):
        if visited[y][x] == 1:
            result += 1
print(result)
