import sys
from heapq import heappush, heappop
sys.stdin = open('1202.txt', 'r')
input = sys.stdin.readline
N, K = map(int, input().split())
jowel = [tuple(map(int, input().split())) for _ in range(N)]
jowel.sort(key=lambda x: x[0], reverse=True)
bag = [int(input()) for _ in range(K)]
bag.sort()
result = [0 for _ in range(K)]

Q = []
for i in range(K):
    while jowel and jowel[-1][0] <= bag[i]:
        heappush(Q, -jowel.pop()[1])
    if Q:
        result[i] = -heappop(Q)
print(sum(result))
