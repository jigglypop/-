
import sys
sys.setrecursionlimit(10 ** 5)
sys.stdin = open('./text/6549.txt', 'r')
input = sys.stdin.readline
dp = [i for i in range(10000)]
def Split():return map(float, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()
MAX = 1000000001
def init(n, s, e):
    if s == e:
        tree[n] = board[s]
        return tree[n]
    M = (s + e) // 2
    return min(init(n * 2, s, M), init(n * 2 + 1, M + 1, e))

def query(S, E):
    if S == E:return board[S]
    M = (S + E) // 2
    Max = max(query(S, M), query(M + 1, E))
    h = min(board[M], board[M + 1])
    w = 2
    s = w * h
    i, j = M, M + 1
    while S < i or j < E:  
        if j == E or S < i and board[i - 1] >= board[j + 1]:
            i -= 1
            w += 1
            h = min(h, board[i])
            s = max(s, w * h)
        else:
            j += 1
            w += 1
            h = min(h, board[j])
            s = max(s, w * h)
    return max(Max, s)

N = Int()
board = [Int() for _ in range(N)]
N = len(board)
board = board[1:]
tree = [0] * (4 * N)
init(1, 0, len(board) - 1)
print(query(0, len(board) - 1))