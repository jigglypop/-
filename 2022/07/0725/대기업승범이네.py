import sys
sys.setrecursionlimit(500000)
sys.stdin = open('./text/17831.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

N = Int()
nums = [0, 0] + List()
board = [0] + List()
tree = [[] for _ in range(N + 1)]
dp = [[0, 0] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
for a in range(2, N + 1):
    b = nums[a]
    tree[b].append(a)

def dfs(u):
    for v in tree[u]:
        dfs(v)
        dp[u][0] += max(dp[v][0], dp[v][1])
    dp[u][1] = dp[u][0]
    for v in tree[u]:
        dp[u][1] = max(dp[u][1], dp[u][0] - max(dp[v][0], dp[v][1]) + (board[u] * board[v]) + dp[v][0])
dfs(1)
print(max(dp[1]))