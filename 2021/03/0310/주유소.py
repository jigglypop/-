import sys
sys.stdin = open("13305.txt", "r")
N = int(input())
E = list(map(int, input().split()))
V = list(map(int, input().split()))
Min = V[0]
result = 0
for i in range(1, N):
    Min = min(Min, V[i-1])
    result += Min * E[i-1]
print(result)
