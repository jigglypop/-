import sys
sys.stdin = open('11047.txt', 'r')
N, K = list(map(int, input().split()))

board = [int(input()) for _ in range(N)]
count = 0
for i in range(N):
    count += K // board[-1-i]
    K = K % board[-1-i]
print(count)
