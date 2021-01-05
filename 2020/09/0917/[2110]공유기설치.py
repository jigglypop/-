import sys
sys.stdin = open('2110.txt', 'r')

N, C = map(int, input().split())
routers = [int(input()) for _ in range(N)]
print(routers)
