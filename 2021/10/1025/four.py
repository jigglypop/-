import sys
sys.stdin = open("./17626.txt", "r")
N = int(input())
MAX = sys.maxsize
dp  = [MAX] * (N + 1)
nums = []
root = int(N ** 0.5) + 1
for i in range(1, root):
    I = i * i
    nums.append(I)
    dp[I] = 1
for i in range(1, N + 1):
    for num in nums:
        if i - num > 0:
            dp[i] = min(dp[i], dp[i - num] + 1)
        else:
            break
print(dp[N])