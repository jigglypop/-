import sys
sys.stdin = open('./text/8958.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())
def L(n, arr):
    if len(arr) == 1:return [n for _ in range(arr[0])]
    return [L(n, arr[1:]) for _ in range(arr[0])]

for _ in range(Int()):
    OX = list(input().strip())
    dp = [0] * len(OX)
    dp[0] = 1 if OX[0] == 'O' else 0
    for i in range(1, len(OX)):
        if OX[i] == 'O':
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = 0
    print(sum(dp))