import heapq
import sys
sys.stdin = open('1916.txt', 'r')
input = sys.stdin.readline
N = int(input())
graph = [[] for _ in range(N+1)]
M = int(input())
for _ in range(M):
    a, b, c = map(int, input().split())
    print(a, b, c)

s, e = map(int,input().split())