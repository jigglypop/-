import sys
sys.stdin = open('9095.txt', 'r')
sys.setrecursionlimit(1000000000)
input = sys.stdin.readline
limit = 10000
DP = [-1] * (limit + 1)
DP[0] = 1


def go(i):
    if DP[i] != -1:
        return DP[i]
    if i == 0:
        return 1
    for j in range(1, 4):
        if i - j >= 0:
            DP[i] += go(i-j)
    return DP[i]


go(120)
print(DP[1:10])
# for j in range(1, 4):
#     for i in range(1, limit+1):
#         if i - j >= 0:
#             DP[i] += DP[i-j]
for _ in range(int(input())):
    n = int(input())
    print(DP[n])
