import sys
sys.stdin = open('9205.txt','r')

t = int(input())
for _ in range(t):
    n = int(input())
    graph = [[] for _ in range(n+1)]
    for _ in range(n+2):
        print(1)

