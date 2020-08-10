import sys
sys.stdin = open('[백준11726]2n타일링.txt', 'r')
n = int(input())

DP = [0] * n
DP[0] = 1
DP[1] = 2
for i in range(2, n):
    DP[i] = DP[i-1] + DP[i-2]
    DP[i] %= 10007
print(DP[-1])
