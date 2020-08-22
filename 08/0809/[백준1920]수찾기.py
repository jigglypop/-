import sys
sys.stdin = open('[백준1920]수찾기.txt', 'r')

N = int(input())
A = set(map(int, input().split()))
M = int(input())
m = list(map(int, input().split()))
for i in m:
    if i in A:
        print(1)
    else:
        print(0)
