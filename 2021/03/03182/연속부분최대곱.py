import sys
sys.stdin = open("2670.txt", "r")
input = sys.stdin.readline
N = int(input())
A = [float(input()) for _ in range(N)]
DP = [A[0]]
for i in range(1, N):
    DP.append(max(DP[i-1] * A[i], A[i]))
print(f'{max(DP):.3f}')
