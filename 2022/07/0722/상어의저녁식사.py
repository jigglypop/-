import sys
sys.stdin = open('./text/1671.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

N = Int()
S = [List() for _ in range(N)]
board = [[] for _ in range(N)]
pred = [-1 for _ in range(N)]

for i in range(len(S)):
    for j in range(len(S)):
        if i == j:
            continue
        if S[i][0] >= S[j][0] and S[i][1] >= S[j][1] and S[i][2] >= S[j][2]:
            if S[i][0] == S[j][0] and S[i][1] == S[j][1] and S[i][2] == S[j][2]:
                if i > j:
                    board[i].append(j)
                else:
                    board[j].append(i)
            else:
                board[i].append(j)

def dfs(u):
    if not check[u]:
        check[u] = True
        for v in board[u]:
            if pred[v] == -1 or dfs(pred[v]):
                pred[v] = u
                return True
        return False

total = 0
for i in range(N):
    for _ in range(2):
        check = [False for _ in range(N)]
        if dfs(i):
            total += 1
print(len(pred) - total)