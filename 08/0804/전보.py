import heapq
import sys

sys.stdin = open("전보.txt", 'r')
n, m, start = map(int, input().split())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)
