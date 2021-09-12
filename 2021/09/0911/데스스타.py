import sys
sys.stdin = open('./11811.txt', 'r')
input = sys.stdin.readline
N = int(input())
result = [0 for _ in range(N)]
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(i + 1, len(temp)):
        result[i] |= temp[j]
        result[j] |= temp[j]
print(*result, end=" ")